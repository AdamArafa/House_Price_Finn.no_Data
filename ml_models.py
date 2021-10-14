# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:43:27 2021

@author: arafa
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data_cleaned_more.csv')

df.columns

# choosing relevant columns

df_model = df[['Prisantydning', 'Fellesgjeld', 'Omkostninger','Felleskost','Boligtype','Soverom', 'Primærrom',
       'Bruksareal', 'Etasje','avstand', 'balkong', 'utsikt', 'garasje', 'heis','parkering', 'hage', 'sentrum',
       'toppleilighet', 'Alder','Energimerking_encoded', 'Aksje', 'Andel', 'Selveier']]

# get dummy data 

df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('Prisantydning', axis=1)
y = df_dum['Prisantydning'].values # .values makes y to be an array instead of Series. this is because arrays are recomended to be used in models

# split the data, 75% for training the model and 25% to test the model

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.2)

# models to test:
    
# 1. multiple linear regression

#statsmodel package
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
print(model.fit().summary())

# the model_summary
# 1. R_squared: 0.897 # this is good, tells that our model explains arround 89% of the variations in the data
# 2. p>|t| is what we want to focus on, so a P-value less than 0.05 means it's significant in our model, 
# so 'Etasje' is not because it has a P_value of 0.649. 'garasje' is significant because it has a P_value of 0.015 which is < 0.05
# seems like appartment with 'garasje', 'hage', 'parkering' are more expensive than these without.
# more details in the summary table**

from sklearn.linear_model import LinearRegression

# creates small train vaildations sets, and apply it to the model, 
# this creates a sense of how the model will perform in reality
from sklearn.model_selection import cross_val_score

mlr_model = LinearRegression()
mlr_model.fit(X_train, y_train)

# 'neg_mean_absolute_error' is a good choise, because its the most representive this will show how far on average off our general prediction
# so if we are on average off by 100 000, that mean we are on average off by 100 000 kr  
# a multiple linear regression is actually abit difficult to get a good value from that because there is such a limited data 
print(np.mean(cross_val_score(mlr_model,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))) 


# 2. random forrest

# here I expect raandom forrest to perform very well, especially because its kind of a tree based decision 
# process and there are a lot of 0, 1 values 
from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor()
print(np.mean(cross_val_score(rf_model,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))) 


# 3. XGBoost

import xgboost as xg
  
# Train and test set are converted to DMatrix objects, as it is required by learning API.
train_dmatrix = xg.DMatrix(data = X_train, label = y_train)
test_dmatrix = xg.DMatrix(data = X_test, label = y_test)
  
# Parameter dictionary specifying base learner
param = {"booster":"gbtree", "objective":"reg:squarederror"}
  
xgb_r = xg.train(params = param, dtrain = train_dmatrix, num_boost_round = 500)
  

# To do after
# 1. tune models GridsearchCV

# now lets tune the model using grid search
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf_model,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

print(gs.best_score_)
print(gs.best_estimator_)

# the model is improved with very small amount


# 2. test ensembles
tpred_mlr_model = mlr_model.predict(X_test)
tpred_rf_model = gs.best_estimator_.predict(X_test)
tpred_xgb_model = xgb_r.predict(test_dmatrix)


# evaluate the models by comparing predictions with actual values
from sklearn.metrics import mean_absolute_error as mae
mae(y_test,tpred_mlr_model)
mae(y_test,tpred_rf_model)
mae(y_test, tpred_xgb_model)

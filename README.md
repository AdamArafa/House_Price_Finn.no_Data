# Residence price estimator based on around 1000 residences scraped from Finn.no: 

## Project Overview
* Scraped data from Finn.no (Norwegian website) using Python/Selenium (Oslo Data). Data from other counties can be used if its of interest.
* Created additional feature (avstand) which is the distance from the Oslo city center using 'Google distance matrix api'
* Created additional features from the residence description.
* Applying different regression models (Linear Regression, Random Forest, and XGBoost) to the data to find the best model.

*Note: The project its not 100% done yet, improvement to the ML models and building a client facing API will be done/added soon.

## Programming Language & Packages
* Python
* Packages: numpy, pandas, matplotlib, seanborn, plotly, statsmodel, sklearn, selenium, XGBoost 

## Data scraped
When scraping the finn.no for residences, the following data was collected for each posted residence (The columns names are in Norwegian language):
* Address
* Prisantydning
* Fellesgjeld
* Omkostninger
* Totalpris
* Felleskost
* Boligtype
* Eieform_bolig
* Soverom
* Primærrom
* Bruksareal
* Etasje
* Byggeår
* Energimerking
* Fasiliteter
* Beskrivelse
* Eiendomsmegler

## Data Cleaning
Before applying the data to the Machine Learning models, some data_cleaning was applied to the data and, some extra features was added.

* Removed all duplicates (321 rows)
* Removed all rows that didn't contain at least 12 valid values (not NaN)
* Swaped values between features (where the data was scraped to wrong feature).
* created 'avstand' (distace). The distance from the city center was calculated using the zipcode of the residence and Oslo train station as my center point. To create this feature 'Google distance matrix api' was used.
* Removed Fasiliteter feature, because the data in this feature wasn't collected correctly.
* Created many features out of the residence description. I beleive this features have affect on the residence price. Some of these features are:
  * Balkong
  * Garasje
  * Heis
  * Utsikt
  * Parkeringplass
 * Used Knn imputer to predict the Energimerking for residences where Energimerking was missing.

## Exploratory Data Analysis (EDA)
Check correlation between Prisantydning and features that i beleive can influence this feature. After running a correlation test I confirmed my hypothesis that Prisantydning and Primærrom have a positive correlation. Also answed some questions that I was interested in.

<img src="newplot (2).png" width="450" height="400"> <img src="newplot (1).png" width="450" height="400"> <img src="newplot (3).png" width="450" height="400"> <img src="newplot (4).png" width="450" height="400"> 

## Models Building
I started by converting the categorical features into dummy features, and then divding the dataset into train and test sets with train size of 80% and test size of 20%.
I build 3 different models and evaluated them using Mean Abslout Error (MAE). I chose MAE because it is relatively easy to understand and explain and outliers aren’t particularly bad in for this type of model.
The models are:
* Multiple Linear Regression
* Random Forest – Because of the sparse data from the many categorical variables.
* XGBoost

## Models Performance
* Random Forest - MAE =  617854.22
* XGBoost - MAE = 638861.23 
* Multiple Linear Regression - MAE = 1186950.01
From the MAE results we can see that RF model outperfoms the other models, XGBoost is second best and MLR model comes last.

as i mentioned before some more work will be done on these models to improve its performace.




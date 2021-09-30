# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:28:59 2021

@author: arafa
"""
import selenium
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver as wb
from tqdm import tqdm
import pandas as pd

webD = wb.Chrome('chromedriver.exe')
webD.get('https://www.finn.no/realestate/homes/search.html?lifecycle=1&location=0.20061&property_type=3&property_type=1&property_type=2&property_type=4&sort=PUBLISHED_DESC')


appartments_urls = []
condition=True


while condition:
    appartments_lst = webD.find_elements_by_class_name('ads__unit')
    for a in appartments_lst:
        # use try except to avoid the program from breaking because of the ads
        # the ads has no tag_name('h2')
        try:
            leilighet_url = a.find_element_by_tag_name('h2').find_element_by_tag_name('a').get_property('href')
            appartments_urls.append(leilighet_url)
        except:
            continue
        try:
            webD.find_element_by_xpath('/html/body/div[2]/main/div[3]/div/div/nav/a/span[1]').click()
        except:
            condition=False
            
# what I want to collect about each appartment
'''
appartment_info = {
    'Address': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[1]/p').text,
    'Prisantydning': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[3]/span[2]').text,
    'Fellesgjeld': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[1]').text,
    'Omkostninger': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[2]').text,
    'Totalpris': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[3]').text,
    'Felleskost': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[3]').text,
    'Boligtype': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[1]').text,
    'Eieform_bolig': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[2]').text,
    'Soverom': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[3]').text,
    'Primærrom': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[4]').text,
    'Bruksareal': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[5]').text,
    'Etasje': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[6]').text,
    'Byggeår': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[7]').text,
    'Energimerking': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[8]/div').text,
    'Beskrivelse': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[1]/h1').text,
    'Eiendomsmegler': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/h2/img').get_property('alt'),
    'Fasiliteter': webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/div/ul').text
    }

appartment_info

'''


all_appartments_details = []

# the code stoped twice. Run the code again from the last readed url. this way tqdm(appartments_urls[520:])
for i in tqdm(set(appartments_urls)):
    
    webD.get(i)
    
    try:
        Address= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[1]/p').text
    except NoSuchElementException:
        Address = -1
    try:
        Prisantydning= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/span[2] ').text
    except NoSuchElementException:
        Prisantydning = -1
    try:
        Fellesgjeld= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[1]').text
    except NoSuchElementException:
        Fellesgjeld = -1
    try:
        Omkostninger= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[2]').text
    except NoSuchElementException:
        Omkostninger = -1
    try:
        Totalpris= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[3]').text
    except NoSuchElementException:
        Totalpris = -1
    try:
        Felleskost= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/div[2]/dl[2]/dd[3]').text
    except NoSuchElementException:
        Felleskost = -1
    try:
        Boligtype= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[1]').text
    except NoSuchElementException:
        Boligtype = -1
    try:   
        Eieform_bolig= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[2]').text
    except NoSuchElementException:
        Eieform_bolig = -1
    try:
        Soverom= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[3]').text
    except NoSuchElementException:
        Soverom = -1
    try:
        Primærrom= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[4]').text
    except NoSuchElementException:
        Primærrom = -1
    try:
        Bruksareal= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[5]').text
    except NoSuchElementException:
        Bruksareal = -1
    try:
        Etasje= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[6]').text
    except NoSuchElementException:
        Etasje = -1
    try:
        Byggeår= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[7]').text
    except NoSuchElementException:
        Byggeår = -1
    try:    
        Energimerking= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/dl/dd[8]/div').text
    except NoSuchElementException:
        Energimerking = -1
    try:
        Beskrivelse= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[1]/h1').text
    except NoSuchElementException:
        Beskrivelse = -1
    try:
        Eiendomsmegler= webD.find_element_by_xpath('/html/body/main/div/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/h2/img').get_property('alt')
    except NoSuchElementException:
        Eiendomsmegler = -1
    try:
        Fasiliteter = webD.find_element_by_xpath('/html/body/main/div/div[4]/div[1]/div/section[2]/div/ul').find_elements_by_tag_name("li")
    except NoSuchElementException:
        Fasiliteter = -1
    
    single_appartment_info = {
        'Address': Address,
        'Prisantydning' :Prisantydning,
        'Fellesgjeld': Fellesgjeld,
        'Omkostninger': Omkostninger,
        'Totalpris': Totalpris,
        'Felleskost': Felleskost,
        'Boligtype': Boligtype,
        'Eieform_bolig': Eieform_bolig,
        'Soverom': Soverom,
        'Primærrom': Primærrom,
        'Bruksareal': Bruksareal,
        'Etasje': Etasje,
        'Byggeår': Byggeår,
        'Energimerking': Energimerking,
        'Fasiliteter': Fasiliteter,
        'Beskrivelse': Beskrivelse,
        'Eiendomsmegler': Eiendomsmegler
        }
    
    all_appartments_details.append(single_appartment_info)


# create pandas dataframe out of the all_appartments_details list
df = pd.DataFrame(all_appartments_details)
df.shape

# save the dataframe 
df.to_csv('scraped_finn_data.csv', index=False)

# reading the saved data file
read_data = pd.read_csv('scraped_finn_data.csv')
read_data.head()

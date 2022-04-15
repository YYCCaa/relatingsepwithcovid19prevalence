# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:20:12 2021

@author: caoyu
"""

'''
The code was intended to transform the dates into numerical values, which is the difference between a date and the first
day of pandemic, so that the file can be used to model the case counts as a function of days after the start of pandemic.
'''

import pandas as pd
 
 
import datetime
import numpy as np
 
 
hospital  = pd.read_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/Copy covid19hospitalbycounty.csv')
cases = pd.read_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/covid19cases_test - covid19cases_test.csv')
 


#hospital1 = hospital.loc[hospital.County.isin(cases.County.unique())]
cases1 = cases.loc[cases.County.isin(hospital.County.unique())]

hospital2 = []
cases2 = []

for area in cases1.County.unique():
    cases2.append(cases1.loc[cases1.County == area,:])
for i in range(len(cases2)):
    w = cases2[i].iloc[0,0].split('/')
    a = cases2[i].iloc[243,0].split('/')
    
    d = datetime.date(int(w[2]),int(w[0]),int(w[1]))
    k = datetime.date(int(a[2]),int(a[0]),int(a[1]))
 
    cases2[i] = cases2[i].iloc[(k-d).days:(datetime.date(2021,4,2)-d).days,:].reset_index()
k = 0
for i in range(len(cases2)):
    for j in range(len(cases2[i].index)):
 
        k = cases2[i].loc[j,'date'].split('/')
            
        da = datetime.date(int(k[2]),int(k[0]),int(k[1]))
    
        cases2[i].loc[j,'date'] = (da - datetime.date(2020,2,1)).days
 
        
 

finale = pd.concat(cases2)
print(cases2[0])
finale.to_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/dateindigit.csv', encoding='utf-8')

 
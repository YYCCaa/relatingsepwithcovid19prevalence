# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:11:41 2022

@author: Yue Cao
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:48:17 2021

@author: Yue Cao
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
First, the program weeds out counties in covid19cases_test - covid19cases_test.csv and vaccinedateorganized.csv that are not
in period 1 - Copy.csv for consistency purposes.

Then, the program combines covid19cases_test - covid19cases_test.csv and vaccinedateorganized.csv that covers the same California counties
but have different columns and cover different time span. For the same county, the space is left blank if there's no data
'''

import pandas as pd
standard = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/period 1 - Copy.csv')
cases  = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/covid19cases_test - covid19cases_test.csv')
hospital = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/vaccinedateorganized.csv')
 


hospital1 = hospital.loc[hospital.County.isin(standard.County.unique())]
cases1 = cases.loc[cases.County.isin(standard.County.unique())]


hospital2 = []
cases2 = []
final = []
 
uniquelist = hospital1.County.unique() 

for area in hospital1.County.unique():
    hospital2.append(hospital1.loc[hospital1.County == area,:]) 
   
for area in cases1.County.unique():
    cases2.append(cases1.loc[cases1.County == area,:]) 
for i in range(0,len(cases1.County.unique())):
    hospital2[i] = hospital2[i].loc[hospital2[i].date.isin(cases2[i].date.unique())]
    print(i)
for i in range(0,len(cases1.County.unique())):
    cases2[i] = cases2[i].set_index('date')     
    hospital2[i] = hospital2[i].set_index('date')   
columnnameappend = hospital1.columns.values.tolist()
columnnameappend.remove('date')

 
 
 
for i in range(len(uniquelist)):
    for j in columnnameappend:
        for k in list(hospital2[i].index.values):
            cases2[i].loc[k,j] = hospital2[i].loc[k,j]

 
 
finale = pd.concat(cases2)
 

 
finale.to_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/vess.csv', encoding='utf-8')
 


















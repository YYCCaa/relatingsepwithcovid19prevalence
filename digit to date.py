# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:18:51 2022

@author: caoyu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:14:46 2022

@author: Yue Cao
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:20:12 2021

@author: Yue Cao
"""
'''
This program converts numerical digits in the date column to date(mm/dd/yyyy). The program is intended to unify date expression.
All dates in the date columns in all csv files were converted to digit using excel, and then they were converted to the
standard date format using this program.
'''

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
 
import seaborn as sns
from datetime import timedelta, datetime
import numpy as np
 
standard = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/period 1.csv')

cases = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/bites.csv')



#hospital1 = hospital.loc[hospital.County.isin(cases.County.unique())]
cases1 = cases 

hospital2 = []
cases2 = []

for area in cases1.county.unique():
    cases2.append(cases1.loc[cases1.county == area,:])

 

count = 0
for i in range(len(cases2)):
    cases2[i] = cases2[i].reset_index()
for i in range(len(cases2)):
    for j in range(len(cases2[i].index)):
        #print(type(cases2[i].loc[j,'date']))
        
        ka = int(cases2[i].loc[j,'date'])
        Begindatestring = '7/27/2020'
        start = datetime.strptime(Begindatestring, "%m/%d/%Y")
 
        cases2[i].loc[j,'date'] = str(start + timedelta(days = ka)).replace('00:00:00','')
        
        #print(cases2[i].loc[:,'pate'])
    
 


finale = pd.concat(cases2)
 
finale.to_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/vaccinedateorganized.csv', encoding='utf-8')

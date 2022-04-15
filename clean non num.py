# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:20:29 2021

@author: caoyu
"""
'''
The program was intended to change all non-numerical data types(due to errors) in specific columns to 0.
'''

import pandas as pd
num = 2
file = pd.read_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/yaesdd3DdD.csv')
file2 = file.iloc[:,num:]

for i in file2.columns.values.tolist():
    file2[i] = pd.to_numeric(file2.loc[:,i].astype(str).str.replace(',',''), errors='coerce').fillna(0).astype(float)
file3 = pd.concat([file.iloc[:,0:num], file2], axis=1)
file3.to_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/work.csv', encoding='utf-8')


'''
for c in range(len(file2.index)):
    for d in range(len(file2.columns.values.tolist())):
        try:
            if((type(file2.iloc[c,d]) != float) & (type(file2.iloc[c,d]) != float)):
                file2.iloc[c,d] = float(file2.iloc[c,d])
        except:
            pass
   
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

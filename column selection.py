# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:39:06 2021

@author: Yue Cao
"""
'''
This program delete the columns in ab.csv that don't exist in period 1.csv for consistency purposes.
'''

import pandas as pd

p1 = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/period 1.csv')
ab= pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/ab.csv')
column = p1.columns.values

columna = ab= .columns.values 

delele = []
for i in columna:
    num= 0
    for j in column:
        if(j == i):
            (num += 1
    if(num == 0):
        delele.append(i)
 
kka.drop(delele, axis=1, inplace=True)
kka.to_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/delete.csv')
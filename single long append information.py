# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:01:47 2021

@author: caoyu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:07:55 2021

@author: caoyu
"""
'''
There's some socioeconomic data associated with a particular county that doesn't change with respect to date. 
This program concatenates such data to period 1 - Copy.csv in a way that, for every county, the concatenated data
is the same for all dates.


'''
import pandas as pd
copy = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/vaccineandcases.csv')
caseloads = pd.read_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/period 1 - Copy.csv')

 
caseloads1 = caseloads.loc[caseloads.County.isin(copy.County.unique())]
countyGov1 = pd.DataFrame([])
countyProfile1 = pd.DataFrame([])
expenditure1 = pd.DataFrame([])
people1 = pd.DataFrame([])
revenue1 = pd.DataFrame([])
taxes1 = pd.DataFrame([])

caseloads2 = []
countyGov2 = []
countyProfile2 = []
expenditure2 = []
people2 = []
revenue2 = []
taxes2 = []

caseloads3 = None
countyGov3 = None
countyProfile3 = None
expenditure3 = None
people3 = None
revenue3 = None
taxes3 = None
caseloads2 = []
copy2 = []

filelist1 = []
filelist2 = [caseloads2,countyGov2,countyProfile2,expenditure2,people2,revenue2,taxes2]
filelist3 = [caseloads3,countyGov3,countyProfile3,expenditure3,people3,revenue3,taxes3]
columnnamelist = []

checklist = [expenditure1,revenue1,caseloads1,countyGov1,countyProfile1,people1,taxes1,copy]

 

for i in range(len(checklist)-1):
    filelist1.append(checklist[i])



theRange = len(filelist1)

for thing in filelist1:
    k = thing.columns.values.tolist()
    columnnamelist.append(k)
for i in columnnamelist:
    try:
        i.remove('County')
    except:
        pass
for area in checklist[-1].County.unique():
    for i in range(0,theRange):
        try:
            filelist2[i].append(filelist1[i].loc[filelist1[i].County == area,:])
            filelist3[i] = pd.concat(filelist2[i], ignore_index=True)
        except:
            pass

for area in checklist[-1].County.unique():
    try:
        copy2.append(checklist[-1].loc[checklist[-1].County == area,:])
    except:
        pass


for i in range(0,len(copy2)):
     
    for j in range(0,theRange):
        for p in range(0,len(columnnamelist[j])):
            try:
                copy2[i].loc[:,columnnamelist[j][p]] = filelist3[j].loc[i,columnnamelist[j][p]]
            except:
                pass
final = pd.concat(copy2)
final.to_csv('C:/Users/redacted/OneDrive/Desktop/Research Dataset/single long append.csv', encoding='utf-8')























 
 
































'''
The program is used to model the case counts as a function of days after the start of pandemic.
'''


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import datetime
import numpy as np
import scipy.optimize as opt
def logistic(t,a,b,c,phi):
    return (c/(1+a*np.exp(-b*t)))+phi
import math
bound = (0, [100000,3,1000000,300000])
print("Setup Complete")
hospital  = pd.read_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/Copy covid19hospitalbycounty.csv')
cases = pd.read_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/period 1 cases.csv')
yes = pd.concat([hospital,cases])


#hospital1 = hospital.loc[hospital.County.isin(cases.County.unique())]
cases1 = cases.loc[cases.County.isin(hospital.County.unique())]

hospital2 = []
cases2 = []
Data = []

for area in cases1.County.unique():
    cases2.append(cases1.loc[cases1.County == area,:])
   
    
    
for i in range(len(cases2)):
        x = np.array(cases2[i]['date'])-243
        
        y = np.array(cases2[i]['cumulative_cases'])
        p0 = np.array([20,2.5,1.3,30000])
        q = 0
        l = 0
        (a,b,c,phi),cov = opt.curve_fit(logistic,x,y,bounds = bound, p0 = p0)
        for j in x:
            for k in y:
                    q += (logistic(j,a,b,c,phi)-k)*(logistic(j,a,b,c,phi)-k)
                    l += k

        Data.append([cases2[i].County.unique()[0],a,b,c,phi,math.sqrt(q)/l])
 
'''        plot2 = plt.figure(i)
        plt.plot(x,logistic(x,a,b,c,phi),"r-")
        plt.scatter(x,y)
        plt.title('Logistic Model vs Real Observation in' + cases2[i].County.unique()[0])
        plt.legend(['logistic Model','Real data'])
        plt.xlabel('Time')
        plt.ylabel('Infections')
     
plt.show()

'''
Datad = pd.DataFrame(Data,columns = ['County','a','b','c','phi','percent deviation'])
Datad.to_csv('C:/Users/caoyu/OneDrive/Desktop/Research Dataset/period 1a.csv', encoding='utf-8')





















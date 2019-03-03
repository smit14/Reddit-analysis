# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 06:14:43 2018

@author: smit
"""
#%%
import numpy as np
import json
#%%

def get_gini(x):
    
    n = len(x)
    num = 0
    for i in range(n):
        for j in range(n):
            num += abs(x[i]-x[j])
    
    den = 2*n*sum(x)
    
    return num/float(den)
#%%
'''
x = np.array([11,0,0,0,0,0,0,0,-1])
print(get_gini(x))
'''
#%%         
with open('./chain_networks/240sx.json') as fp:
    months_net = json.load(fp)

gini = np.zeros([11])    
for i in range(11):
    
    net = months_net[i]
    keys = net.keys()
    
    n = len(keys)
    x = np.zeros([n])
    
    for j in range(n):
        x[j] = len(net[keys[j]])
    
    gini[i] = get_gini(x)
    
#%%
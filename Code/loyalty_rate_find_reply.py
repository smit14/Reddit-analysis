# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:23:26 2018

@author: smit
"""

'''

loyalty rate for reply networks

'''
#%%
import numpy as np
#%%
loyal_users = np.load('loyal_users.npy').item()
#%%
loyalty_rate = np.zeros([2046,9])
files = loyal_users.keys()

for i in range(2046):
    x = loyal_users[files[i]]
    for j in range(9):
        ls_current = set(x[j])
        ls_next = set(x[j+1])
        if len(ls_current)!=0:
            loyalty_rate[i,j] = len(ls_current.intersection(ls_next))/float(len(ls_current))
#%%
#loyalty_rate = loyalty_rate[:,:9]

#%%
loyalty_rate__dict = {}

for i in range(2046):
    loyalty_rate__dict[files[i]] = loyalty_rate[i,:]
#%%
        
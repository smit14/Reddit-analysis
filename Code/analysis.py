# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:36:10 2018

@author: smit
"""
'''
inference

'''
#%%
import numpy as np

loyalty_rate = np.load('loyalty_rate.npy').item()
graph_params = np.load('graph_params_reply.npy').item()
gini_coeff = np.load('gini_coeff.npy').item()

#%%

keys = loyalty_rate.keys()
mean_loyalty_rate = {}

for i in range(2046):
    mean_loyalty_rate[keys[i]] = np.mean(loyalty_rate[keys[i]])
    
#%%
    
import operator
sorted_loyalty = sorted(mean_loyalty_rate.items(), key=operator.itemgetter(1))
#%%
sorted_loyalty_reverse = sorted(mean_loyalty_rate.items(), key=operator.itemgetter(1),reverse = True)
#%%

loyalty = np.zeros([2046])
density = np.zeros([2046])
cc = np.zeros([2046])
asrt = np.zeros([2046])
triads = np.zeros([2046])
gini = np.zeros([2046])

for i in range(2046):
    
    loyalty[i] = sorted_loyalty_reverse[i][1]
    gpi = graph_params[sorted_loyalty_reverse[i][0]]
    
    density[i] = np.mean(gpi[:,0])
    cc[i] = np.mean(gpi[:,2])
    asrt[i] = np.mean(gpi[:,1])
    triads[i] = np.mean(gpi[:,3])
    
    gini[i] = np.mean(gini_coeff[sorted_loyalty_reverse[i][0]])
    
    
#%%
import matplotlib.pyplot as plt
n, bins, patches =plt.hist(x=loyalty, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('loyalty rate of reddit communities')
plt.ylabel('Frequency')
plt.title('frequency distribution of communities')
maxfreq = n.max()
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
#%%

plt.plot(loyalty)
plt.grid(axis='both', alpha=1)
plt.xlabel('communities (in descending order of loyalty rate)')
plt.ylabel('loyalty rate')
plt.title('average loyalty rate of all subreddit communities')
plt.show()
#%%
dens = density
dens[density>0.15] = 0.15
plt.plot(dens)
plt.grid(axis='both', alpha=1)
plt.xlabel('communities (in descending order of loyalty rate)')
plt.ylabel('density')
plt.title('average density of subreddit user interaction graph')
plt.show()
#%%
plt.plot(cc)
plt.grid(axis='both', alpha=1)
plt.xlabel('communiies (in descending order of loyalty rate)')
plt.ylabel('clustering coeeficient')
plt.title('average clustering coefficient of subreddit user interaction graph')
plt.show()
#%%
plt.plot(asrt)
plt.grid(axis='both', alpha=1)
plt.xlabel('communiies (in descending order of loyalty rate)')
plt.ylabel('assortativity')
plt.title('average assortativity of subreddit user interaction graph')
plt.show()
#%%
plt.plot(triads)
plt.grid(axis='both', alpha=1)
plt.xlabel('communiies (in descending order of loyalty rate)')
plt.ylabel('Number of triangles')
plt.title('average number of triangles of subreddit user interaction graph')
plt.show()

#%%

#%%
plt.plot(gini)
plt.grid(axis='both', alpha=1)
plt.xlabel('communiies (in descending order of loyalty rate)')
plt.ylabel('Gini coefficient')
plt.title('average Gini coefficient of subreddit user interaction graph')
plt.show()

#%%

plt.boxplot([density[0:1023],density[1023:]], sym='',labels = ['Loyal', 'Unloyal'])
plt.title('difference in desity for loyal and unloyal communities')
#%%

plt.boxplot([cc[0:1023],cc[1023:]], sym='',labels = ['Loyal', 'Unloyal'])
plt.title('difference in clustering coefficient for loyal and unloyal communities')

#%%

plt.boxplot([asrt[0:1023],asrt[1023:]], sym='',labels = ['Loyal', 'Unloyal'])
plt.title('difference in assortativity for loyal and unloyal communities')

#%%

plt.boxplot([gini[0:1023],gini[1023:]], sym='',labels = ['Loyal', 'Unloyal'])
plt.title('difference in inequality for loyal and unloyal communities')

#%%


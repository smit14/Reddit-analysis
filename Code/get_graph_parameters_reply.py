# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:18:26 2018

@author: smit
"""

'''

structural properties of graph

density
clustering coefficient
assortativity
number of triads

'''
#%%
import numpy as np
import json
import snap 
import networkx as nx
import os
#%%


files = os.listdir('./chain_networks/')
dir_c = './reply_networks/'
n = len(files)


#%%
def get_dict(net):
    
    user_dict= {}
    user_set = set()    
    keys = net.keys()
    
    for i in range(len(net)):
        user_set.add(keys[i])
        ls = net[keys[i]]
        for j in range(len(ls)):
            user_set.add(ls[j])
    
    user_list = list(user_set)
    count = 0
    for i in range(len(user_list)):
        user_dict[user_list[i]] = count
        count+=1
    
    return user_dict
    #%%
def get_graph_parameters(file_name):
    
    '''
    11 months
    4 parameters: density ,assortativity,clustering coefficient, , number of triads
    
    '''
    params = np.zeros([11,4])       
    with open(file_name) as fp:
        month_nets = json.load(fp)

    for ii in range(11):
        network = month_nets[ii]
        keys = network.keys()
        usr_dict = get_dict(network)
        
        G = nx.DiGraph()
        
        for i in range(len(usr_dict)):
            G.add_node(i)

        for i in range(len(network)):
            ls = network[keys[i]]
            for j in range(len(ls)):
                G.add_edge(usr_dict[keys[i]],usr_dict[ls[j]])

        e = G.number_of_edges()
        v = G.number_of_nodes()
        
        density = e/float((v*(v-1)))
        assort = nx.algorithms.assortativity.degree_assortativity_coefficient(G)
        cc = nx.algorithms.average_clustering(G)
        
        
        Gb = snap.TNGraph.New()
        keys_b = usr_dict.keys()

        for i in range(len(usr_dict)):
            Gb.AddNode(i)

        for i in range(len(network)):
            ls = network[keys[i]]
            for j in range(len(ls)):
                Gb.AddEdge(usr_dict[keys[i]],usr_dict[ls[j]])
        
        triads = snap.GetTriads(Gb)
        
        params[ii,0] = density
        params[ii,1] = assort
        params[ii,2] = cc
        params[ii,3] = triads
    
    return params
#%%
    
  
    params_r = {}
    
    for i in range(n):
        print(i)
        params_r[files[i]] = get_graph_parameters(dir_c+files[i])
    
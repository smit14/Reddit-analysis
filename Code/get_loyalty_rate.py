# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 01:58:53 2018

@author: smit
"""

'''
returns loyalty rate
'''

#%%
import numpy as np
import json

dir_c = './reply_networks/'

#%%
user_community_list = np.load('user_community.npy').item()

#%%

def get_number_from_json(usr_id,json_name,m):
    
    with open(dir_c+json_name) as fp:
        months_net = json.load(fp)
    #print(usr_id)
    #print(json_name)
    cmnt_num = len(months_net[m][usr_id])
    
    return cmnt_num
    
#%%
    
def get_comment_numbers(usr_id,m):
    user_ac = user_community_list[usr_id][m]
    cmnt_ls = np.zeros([len(user_ac)])
    for i in range(len(user_ac)):   
        cmnt_ls[i] = get_number_from_json(usr_id,user_ac[i],m)
    
    return cmnt_ls
    
#%%
    
def get_loyal_users(ind,months_net,m):
    
    ls = []
    month_dict = months_net[m]
    month_keys = month_dict.keys()
    
    next_month_dict = months_net[m+1]
    next_month_keys = next_month_dict.keys()

    count = 0
    
    for i in range(len(month_dict)):
        #print('month: %d, count_u: %d'%(m,count))
        
        usr_id = month_keys[i]
        
        if usr_id in next_month_keys:
            cmnt_n = get_comment_numbers(usr_id,m)
            next_cmnt_n = get_comment_numbers(usr_id,m+1)
            
            current_cmnt = len(month_dict[usr_id])
            next_cmt = len(next_month_dict[usr_id])
            
            flag1 = 0
            flag2 = 0  
    # if we consider 50% of comments are necessary to tell that user prefers that community        
            sum_cmnt = sum(cmnt_n)
            sum_next_cmnt = sum(next_cmnt_n)
            
            if current_cmnt/sum_cmnt > .5:
                flag1 = 1
            if flag1 == 1:
                if next_cmt/sum_next_cmnt > .5:
                    flag2 = 1
            
            if flag1 + flag2 == 2:
                ls.append(usr_id)
                count += 1
    
    return ls
 #%%   
def get_loyalty_rate(file_name):
    
    with open(dir_c+file_name) as fp:
        month_nets = json.load(fp)
    
    loyal_users = []
    
    for i in range(10):
        print(i)
        ls = get_loyal_users(file_name,month_nets,i)
        lset = set(ls)
        loyal_users.append(lset)
    
    arr = np.zeros(10)
    for i in range(10):
        arr[i] = len(loyal_users[i].intersection(loyal_users[i+1]))
        
    loyalty_rate = np.mean(arr)
    
    return loyalty_rate
    
  #%%
    
print(get_loyalty_rate('240sx.json'))
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:48:31 2020

@author: A8DPDZZ
"""
from scipy.stats import norm

"""
Define Parameters
"""
p = 0.5 #population proportion at 50% - most conservative
M = 0.05 #margin of error at 5%
N = 80 #lot size
Z_p = 0.95 #confidence level
a = (1-Z_p)/2
Z = norm.ppf(1-a) #Inverse CDF of standard normal dist

SS = (((Z**2)*(p * (1-p)))/(M**2)) / (1 + ((Z**2 * p * (1-p)/ ((M**2) * N))))
print("User Input")
print("Sample Size: ", SS, "at", Z_p, "CL")

"""
Population Proportion Sensitivity 
"""
prop_lst = []
prop_aly = [0.5, 0.4, 0.3, 0.2, 0.1, 0.05] #list with various pop. proportion starting at most conservative, use priors if known
def popsens(M, N, Z_p):
    print("Population Proportion Sensitivity")
    for i, num in enumerate(prop_aly):
        a = (1-Z_p)/2
        Z = norm.ppf(1-a) #Inverse CDF of standard normal dist
        SS_p = (((Z**2)*(num * (1-num)))/(M**2)) / (1 + ((Z**2 * num * (1-num)/ ((M**2) * N))))
        prop_lst.append(SS_p)
        print("Pop.Prop: ", num, "Samp. Size: ", SS_p, 
              "with Lot: ", N, "at CL: ", Z_p)
        #return num , SS_p
popsens(M, N, Z_p)

"""
Confidence Level Sensitivity
"""
conf_lst = []
conf_lev = [0.80, 0.85, 0.90, 0.95, 0.975, 0.99] #list with various confidence levels, least conservative
def conflev(p, M, N):
    print("Confidence Level Sensitivity")
    for j, run in enumerate(conf_lev):
        a = (1-run)/2
        Z = norm.ppf(1-a) #Inverse CDF of standard normal dist
        SS_p = (((Z**2)*(p * (1-p)))/(M**2)) / (1 + ((Z**2 * p * (1-p)/ ((M**2) * N))))
        conf_lst.append(SS_p)
        print("Pop.Prop: ", p, "Samp. Size: ", SS_p, 
              "with Lot: ", N, "at CL: ", run)
        #return run, SS_p
conflev(p, M, N)

"""
Error Margin Sensitivity
"""
err_lst =[]
err_Marg = [0.05, 0.06, 0.07, 0.08, 0.08, 0.09]
def marges(p, N, Z_p):
    
 





        


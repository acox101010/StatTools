# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:48:31 2020
@author: A8DPDZZ
"""
from scipy.stats import norm
import argparse

"""
Define Parameters
"""
p = 0.5 #population proportion at 50% - most conservative
M = 0.05 #margin of error at 5%
N = 80 #lot size 
Z_p = 0.95 #confidence level
a = (1-Z_p)/2 #alpha
Z = norm.ppf(1-a) #Inverse CDF of standard normal dist (critical value)
SS = (((Z**2)*(p*(1-p)))/(M**2))/(1+((Z**2*p*(1-p)/((M**2)*N)))) #sample size calculation
print("User Input Values")
print("Sample Size: ", round(SS, 2), "Confidence Level: ", Z_p, "Error: ", M)

if SS > N*a:
    print("Applying FPC to Sample Size...")
    n_c = ((SS*N)/(N+(SS-1)))
    print("Corr. Sample Size: ", round(n_c, 2), "Confidence Level: ", Z_p, "Error: ", M)
else:
    print("FPC to SS not needed")

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
        SS_p = (((Z**2)*(num*(1-num)))/(M**2))/(1+((Z**2*num*(1-num)/((M**2)* N))))
        prop_lst.append(round(SS_p, 2))
        print(i, "Pop.Prop: ", num, "Samp. Size: ", round(SS_p, 2), 
              "Lot size: ", N, "at CL: ", Z_p, "Error: ", M)
        #return num , SS_p
popsens(M, N, Z_p)

"""
Confidence Level Sensitivity
"""
conf_lst = []
conf_lev = [0.99, 0.975, 0.95, 0.90, 0.85, 0.80] #list with various confidence levels, most conservative
def conflev(p, M, N):
    print("Confidence Level Sensitivity")
    for j, run in enumerate(conf_lev):
        a = (1-run)/2
        Z = norm.ppf(1-a) #Inverse CDF of standard normal dist
        SS_p = (((Z**2)*(p*(1-p)))/(M**2))/(1+((Z**2*p*(1-p)/((M**2)*N))))
        conf_lst.append(round(SS_p, 2))
        print(j, "Pop.Prop: ", p, "Samp. Size: ", round(SS_p, 2), 
              "Lot size: ", N, "at CL: ", run, "Error: ", M)
        #return run, SS_p
conflev(p, M, N)

"""
Error Margin Sensitivity
"""
err_lst =[]
err_Marg = [0.05, 0.06, 0.07, 0.08, 0.08, 0.09, 0.10]
def marg(p, N, Z_p):
    print("Error Margin Sensitivity")
    for k, sun in enumerate(err_Marg):
        a = (1-Z_p)/2
        Z = norm.ppf(1-a) #Inverse CDF of standard normal dist
        SS_p = (((Z**2)*(p*(1-p)))/(sun**2))/(1+((Z**2*p*(1-p)/((sun**2)*N))))
        err_lst.append(round(SS_p, 2))
        print(k, "Pop.Prop: ", p, "Samp. Size: ", round(SS_p, 2), 
              "Lot size: ", N, "at CL: ", Z_p, "Error: ", sun)
marg(p, N, Z_p)


        
 





        


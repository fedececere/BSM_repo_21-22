#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:12:57 2022

@author: chiaramarzi
"""
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")

'''def my_plot():
    # TO COMPLETE'''
    
# Sodium parameters  
ki_Na =1.5 
g_Na = 0.02
u_Na =0.107
ke_Na = ki_Na*g_Na

# Urea parameters 
ki_U =0.77
g_U =1
u_U =0.75
ke_U =ki_U*g_U

# Potassium parameters 
ki_K =1.5
g_K = 28.2
u_K = 0.045
ke_K = ki_K*g_K

# Other parameters
qf =2/4/60 #COMPLETE # Ultradiffusion
I = 0 # TO COMPLETE  # Patient is not drinking
'''Assumendo che la dialisi duri 4 ore e sapendo il peso del paziente (70 kg):'''
Vp = 70*58/100+2# TO COMPLETE   # Patient's liquid volume at the begenning of the dialysis
d =0.241# TO COMPLETE # dialysance
cd_Na =140 # TO COMPLETE # Na in dialysis bath
cd_U =0# TO COMPLETE0 # Urea in dialysis bath
cd_K = 2# TO COMPLETE # K in dialysis bath

# Euler's method initialization (remember that time is in minutes)
dt = 0.1  
t_start = 0
t_end = 4*60 
t = np.arange(t_start, t_end+dt, dt) 
L = np.size(t) 

Mi_Na = np.zeros(L)
Me_Na = np.zeros(L)
Mi_U = np.zeros(L)
Me_U = np.zeros(L)
Mi_K = np.zeros(L)
Me_K = np.zeros(L)
ci_Na = np.zeros(L)
ce_Na = np.zeros(L)
ci_U = np.zeros(L)
ce_U = np.zeros(L)
ci_K = np.zeros(L)
ce_K = np.zeros(L)
Vi = np.zeros(L)
Ve = np.zeros(L)
osmi = np.zeros(L)
osme = np.zeros(L)

# Initial conditions
Vi[0] = Vp*5/8# TO COMPLETE
Ve[0] = Vp*3/8# TO COMPLETE

ce_Na[0] =144 # TO COMPLETE
ci_Na[0] = g_Na*ce_Na[0]+u_Na/ki_Na# TO COMPLETE
Mi_Na[0] = ci_Na[0]*Vi[0]# TO COMPLETE
Me_Na[0] = ce_Na[0]*Ve[0]# TO COMPLETE

ce_U[0] = 20# TO COMPLETE
ci_U[0] = g_U*ce_U[0]+u_U/ki_U# TO COMPLETE
Mi_U[0] = ci_U[0]*Vi[0]# TO COMPLETE
Me_U[0] = ce_U[0]*Ve[0]# TO COMPLETE

ce_K[0] =4.5 # TO COMPLETE
ci_K[0] = g_K*ce_K[0]+u_K/ki_K# TO COMPLETE
Mi_K[0] = ci_K[0]*Vi[0]# TO COMPLETE
Me_K[0] = ce_K[0]*Ve[0]# TO COMPLETE

# Osmolarity
osm0= 280# TO COMPLETE
kf = 0.1# TO COMPLETE
ceqi =osm0/0.93-ci_K-ci_Na-ci_U # TO COMPLETE
ceqe = osm0/0.93-ce_K-ce_Na-ce_U# TO COMPLETE
'''in this specific case equal to osm0'''
osmi[0] = (ci_K+ci_Na+ci_U)*0.93# TO COMPLETE
osme[0] =(ce_K+ce_Na+ce_U)*0.93# TO COMPLETE

for j in range(L-1):
    dVi=kf*(osmi[j]-osme[j])
    dVe=I-qf-kf*(osmi[j]-osme[j])
    Vi[j+1]=Vi[j]+dVi*dt
    Ve[j+1]=Ve[j]+dVe*dt
    dMi_Na=-ki_Na*ci_Na[j]+ke_Na[j]+u_Na
    dMe_Na=ki_Na*ci_Na[j]-ke_Na*ce_Na[j]-d*(ce_Na[j]-cd_Na)-qf*ce_Na[j]
    Mi_Na[j+1]=Mi_Na[j]+dMi_Na*dt
    Me_Na[j+1]=Me_Na[j]+dMe_Na*dt
    ci_Na[j+1]=Mi_Na[j+1]/Vi[j+1]
    ce_Na[j+1]=Me_Na[j+1]/Ve[j+1]

    '''repeat for urea and potassium, do osmolarity'''
    osmi[j+1]=(ci_Na[j+1]+ci_U[j+1]+ci_K[j+1]+ceqi)*0.93
    osme[j+1]=(ce_Na[j+1]+ce_U[j+1]+ce_K[j+1]+ceqe)*0.93


    



# plots
# TO COMPLETE

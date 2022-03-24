#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:44:47 2022

@author: chiaramarzi
"""

# Complete the libraries importation
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#def my_plot(x, y, color, title, xlabel, ylabel):
    

# Compliances values from Table III of Albanese et al., 2016
Cl = 0.00127
Ct = 0.00238
Cb = 0.0131
CA = 0.2
Ccw = 0.2245
# Unstressed volumes from Table III of Albanese et al., 2016, needs to be converted from mL to L
Vul = 34.4/1000
Vut = 6.63/1000
Vub = 18.7/1000
VuA = 1.263/1000
# Resistances values from Table III of Albanese et al., 2016
Rml = 1.021
Rlt = 0.3369
Rtb = 0.3063
RbA = 0.0817


# Simulation of 20 seconds 
#to do the simulation we need to define a vector of time
dt = 0.002 #really low because the values of compliances we want to prevent instability
#now let's define the time
t_start=0
t_end=20
t= np.arange(t_start,t_end+dt, dt)
L=np.size(t)
# State variables
''' we define the state variables this way because we want to integrate them. We define a space
of L+1 dimensions because we need also the space for the initial conditions(e already know them for
the auxiliary variables and the volumes)'''
P1 = np.zeros(L+1)
P2 = np.zeros(L+1)
P3 = np.zeros(L+1)
P4 = np.zeros(L+1)
P5 = np.zeros(L+1)

# Auxiliary variables
Pl = np.zeros(L)
Ppl = np.zeros(L)
Pt = np.zeros(L)
Pb = np.zeros(L)
PA = np.zeros(L)

# Volumes
Vl = np.zeros(L)
Vt = np.zeros(L)
Vb = np.zeros(L)
VA = np.zeros(L)
VD = np.zeros(L)

# Natural breath definition
T = 5 # period of the natural breath
Pm=zeros(L) #Pm has the same lenght of the others
#Pmus=-6*sin(2*np.pi/T*t) can also be written as -3+3*np.cos(2*np.pi/T*t)
#we define the amplitude Amus and write
Amus=3
Pmus=Amus*(np.cos(2*np.pi/T*t)-1)
# Initial conditions: now we define the conditions typycal of natural breathing, along with the muscle pressure
Ppl[0]=-5 #♣at the end is -5, so it's still -5 at the beginning of the next one
P5[0]=Ppl[0]-Pmus[0] #knowing ppl and pmus in 0 we can calculate P5
Va[0]=2.3-VuA
P4[0]=Va[0]/CA


for j in range(L):
    Pl[j]=Pl[j]
    Ppl[j]=P5[J]+Pmus[j]
    Pt[j]=P2[j]+Ppl[j]
    Pb[j]=P3[j]+Ppl[j]
    pa[j]=P4[j]+Ppl[J]

    Vl[j]=Cl*Pl[j]*Vu[l] 
    Vt[j]=Ct*(Pt[j]-Ppl[J])+Vut
    Vb[j]=Cb*(Pb[j]-Ppl[j]+Vub)
    Va[j]=CA*(Pb[j]-Ppl[j]-VuA)
    Vd[j]=Vl[j]+vt[j]+Vb[j]
    
    dP1=1/Cl*((Pm[j]-Pl[J])/Rml-(Pl[j]-Pt[j])/Rlt)
    dP2=1/Ct*((Pl[j]-Pt[J])/Rlt-(Pt[j]-Pb[j])/Rtb)
    dP3=1/Cb*((Pt[j]-Pb[J])/Rtb-(Pb[j]-Pa[j])/RbA)
    dP4=1/CA*((Pb[j]-PA[J])/RbA)
    dP5=1/Ccw*((Pl[j]-Pt[J])/Rlt)
    
    p1[J+1]=p1[j]+dP1*dt #DA FINIRE
# Pressures plots

# Volumes plots


# Alveolar ventilation  (at equilibrium)
Vent = 
print("Ventiliation:", Vent)

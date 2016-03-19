# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:14:12 2016

@author: AF
"""

import matplotlib.pyplot as plt
import math
MAX = 100

def initialize(nuclei_a,nuclei_b,t):
    nuclei_a[0]=float(raw_input('initial number of N_a:'))
    nuclei_b[0]=float(raw_input('initial number of N_b:'))
    tc_a=float(raw_input('time constant for particle_a:'))
    tc_b=float(raw_input('time constant for particle_b:'))
    dt=float(raw_input('time step:'))
    t[0]=0.0
    return nuclei_a,nuclei_b,t,tc_a,tc_b,dt


def calculate(nuclei_a,nuclei_b,true_a,true_b,t,tc_a,tc_b,dt):
    alpha = tc_b/tc_a
    A = (nuclei_a[0]*alpha-nuclei_b[0])/(alpha+1)
    B = (nuclei_a[0]+nuclei_b[0])/(alpha+1)
    for i in range(MAX-1):
        nuclei_a[i+1] = nuclei_a[i] + ((nuclei_b[i]/tc_b)-(nuclei_a[i]/tc_a))*dt
        nuclei_b[i+1] = nuclei_b[i] + ((nuclei_a[i]/tc_a)-(nuclei_b[i]/tc_b))*dt
        true_a[i+1] = A*math.exp(-t[i]*(tc_b/tc_a+1)/tc_b)+B
        true_b[i+1] = -A*math.exp(-t[i]*(tc_b/tc_a+1)/tc_b)+B*alpha
        t[i+1] = t[i]+dt
    return nuclei_a,nuclei_b,true_a,t
    
def store(nuclei_a,nuclei_b,t):
    data = open('data.txt','w')
    for i in range(MAX):
        data.write(str(t[i]))
        data.write(' ')
        data.write(str(nuclei_a[i]))
        data.write(' ')
        data.write(str(nuclei_b[i]))
        data.write('\n')
    data.close
    
def draw_figure(nuclei_a,nuclei_b,True_A,True_B,t,tc_a,tc_b,dt):
    plt.figure(figsize=(10,6),dpi=144)
    plt.plot(t,nuclei_a,'*',label='Nuclei_a(numerical)')
    plt.plot(t,True_A,'k',label='Nuclei_a(true)'+' '+r'$A\exp(-\kappa*t)+B$')
    plt.plot(t,nuclei_b,'^',label = 'Nuclei_b(numerical)')
    plt.plot(t,True_B,'r',label='Nuclei_b(true)'+' '+r'$-C\exp(-\kappa*t)+D$')
    plt.xlabel('Time(s)')
    plt.ylabel('Number of Nuclei')
    plt.text(3,0.8*nuclei_a[0],'Time Constant(a) ='+str(tc_a)+'s'+'\n'+'Time Constant(b) ='+str(tc_b)+'s'+'\n'+'Time Step ='+str(dt)+'s')
    plt.legend(loc = 'lower right',fontsize = 8)
    plt.savefig('chapter1_extend_0.05.png',dpi=144)
    plt.show()
    
        
def main():
    n_a = [0]*MAX
    n_b = [0]*MAX
    t = [0]*MAX
    true_a=[0]*MAX
    true_b=[0]*MAX
    (n_a,n_b,t,tau_a,tau_b,dt)=initialize(n_a,n_b,t)
    true_a[0] = n_a[0]
    true_b[0] = n_b[0]
    calculate(n_a,n_b,true_a,true_b,t,tau_a,tau_b,dt)
    store(n_a,n_b,t)
    draw_figure(n_a,n_b,true_a,true_b,t,tau_a,tau_b,dt)
    
main()
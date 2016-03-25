# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:09:36 2016

@author: AF
"""

import ode as solving_ode
import matplotlib.pyplot as plt

A = solving_ode.ode(0.1,0,2,5)  ##### setting the initial population N(0) = 10
A.set_fx('N',['t','N'])
eulerplus_record = A.euler()
rgkt_3_record = A.rgkt_3()
plt.figure(figsize = (10,6))
plt.plot(eulerplus_record[0],eulerplus_record[1][0],'*',label = 'simple euler method')
plt.plot(rgkt_3_record[0],rgkt_3_record[1][0],label = '3rd Runge-Kutta method')
plt.legend()
plt.savefig('chapter1_1.6.png',dpi = 144)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:09:36 2016

@author: AF
"""

import ode as solving_ode
import matplotlib.pyplot as plt
import math

A = solving_ode.ode(0.005,3.8,4,(2,8))  ##### setting the initial population N(0) = 10
A.set_fxs(('y1','-x*y+y1*math.e**x+3*math.sin(2*x)'),'x',('y','y1'))
eulers_record = A.eulers()
rgkt_3s_record = A.rgkt_3s()
plt.figure(figsize = (10,6))
plt.plot(eulers_record[0],eulers_record[1][0],'*',label = 'simple euler method')
plt.plot(rgkt_3s_record[0],rgkt_3s_record[1][0],label = '3rd Runge-Kutta method')
plt.legend(loc = 'left upper')
plt.savefig('example2.png',dpi = 144)
plt.show()
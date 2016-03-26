# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:09:36 2016

@author: AF
"""

import ode as solving_ode
import matplotlib.pyplot as plt
import math

A = solving_ode.ode(0.005,3.8,4,(2,8))  
A.set_fx(('y1','-x*y+y1*math.e**x+3*math.sin(2*x)'),['x','y','y1'])
<<<<<<< HEAD
=======
euler_record = A.euler()
>>>>>>> origin/master
rgkt_3_record = A.rgkt_3()
B = solving_ode.ode(0.005,3.8,4,(2,8))
B.set_fx(('y1','-x*y+y1*math.e**x+3*math.sin(2*x)'),['x','y','y1'])
euler_record = B.euler()
plt.figure(figsize = (10,6))
plt.plot(euler_record[0],euler_record[1][0],label = 'simple euler method')
plt.plot(rgkt_3_record[0],rgkt_3_record[1][0],label = '3rd Runge-Kutta method')
plt.legend(loc = 'left upper')
plt.savefig('example2.png',dpi = 144)
plt.show()

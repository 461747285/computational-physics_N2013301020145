# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 09:08:06 2016

@author: AF
"""

import ode as solving_ode
import matplotlib.pyplot as plt
import math


A = solving_ode.ode(0.01,0,0.5,100)
A.set_fx('10*y',['x','y'])
rgkt_3_record1 = A.rgkt_3()[:]
euler_record = A.euler()[:]
A.set_fx('10*y - 0.01*y**2',['x','y'])
rgkt_3_record2 = A.rgkt_3()[:]
A.set_fx('10*y - 0.04*y**2',['x','y'])
rgkt_3_record3 = A.rgkt_3()[:]
A.set_fx('10*y - 0.07*y**2',['x','y'])
rgkt_3_record4 = A.rgkt_3()[:]
A.set_fx('10*y - 0.12*y**2',['x','y'])
rgkt_3_record5 = A.rgkt_3()[:]
A.set_fx('10*y - 0.16*y**2',['x','y'])
rgkt_3_record6 = A.rgkt_3()[:]
b = 0
y = [100]
euler_2nd = [100]
for i in range(1,len(rgkt_3_record1[0])):
    y.append((10*100*math.e**(10*rgkt_3_record1[0][i]))/(10 - b*100 + b*100*math.e**(10*rgkt_3_record1[0][i])))
    euler_2nd.append(euler_2nd[i - 1] + (10*euler_2nd[i - 1] - b*euler_2nd[i - 1]**2)*0.01 + 0.5*(10 - 2*euler_2nd[i - 1]*b)*(10*euler_2nd[i - 1] - b*euler_2nd[i - 1]**2)*(0.01)**2)
plt.figure(figsize = (10,6))
plt.ylabel('Population',fontsize = 11)
plt.xlabel('Time', fontsize = 11)
plt.plot(rgkt_3_record1[0],euler_record[1][0],linewidth = 2,label = 'simple euler method')
plt.plot(rgkt_3_record1[0],y,linewidth = 2,label = 'exact silution')
plt.plot(rgkt_3_record1[0],euler_2nd,':',linewidth = 5,label = 'corrected simple euler')
plt.plot(rgkt_3_record1[0],rgkt_3_record1[1][0],'k--',linewidth = 3,label = '3rd Runge-Kutta method')
#plt.plot(rgkt_3_record2[0],rgkt_3_record2[1][0],linewidth = 3,label = 'b = 0.01')
#plt.plot(rgkt_3_record3[0],rgkt_3_record3[1][0],linewidth = 3,label = 'b = 0.04')
#plt.plot(rgkt_3_record4[0],rgkt_3_record4[1][0],linewidth = 3,label = 'b = 0.07')
#plt.plot(rgkt_3_record5[0],rgkt_3_record5[1][0],linewidth = 3,label = 'b = 0.12')
#plt.plot(rgkt_3_record6[0],rgkt_3_record6[1][0],linewidth = 3,label = 'b = 0.16')
plt.legend(loc = 'upper left',fontsize = 12)
plt.savefig('chapter1_1.6_.png',dpi = 144)
plt.show()

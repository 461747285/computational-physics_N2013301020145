# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:11:36 2016

@author: AF
"""

import numpy as np
import matplotlib.pyplot as plt
import ode as solving_ode


###  -------- circular orbit -----------------
'''A = solving_ode.ode(0.01,0,1,(1,0,0,2*np.pi))
A.set_fx(['vx','-4*np.pi**2*x/(np.sqrt(x**2+y**2))**3','vy','-4*np.pi**2*y/(np.sqrt(x**2+y**2))**3'],['t','x','vx','y','vy'])
data_record = A.rgkt_4()
plt.figure(figsize = (8,8))
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.plot(data_record[1][0],data_record[1][2])
plt.show()'''

### -------- numerical method ----------------
'''A = solving_ode.ode(0.01,0,2*np.pi,(1,0))
A.set_fx(['v','(2.0/r)*v**2+r-1.5*r**2'],['t','r','v'])
e = 1 - 1./1.5
data_record = A.rgkt_4()
theta=np.arange(0,2*np.pi,0.02)
plt.figure(figsize = (8,6))
plt.subplot(111,polar = True)
plt.plot(data_record[0],data_record[1][0],lw=2, label = 'numerical solution')
plt.plot(theta,(1- e)/(1 - e*np.cos(theta)),'--', linewidth = 3, label = 'theoretical solution')
plt.legend()
plt.savefig('chapter4_4.11_1.png',dpi = 144)
plt.show()'''


###  -------Precession: elliptical orbit ---------------- ## r_max = 0.47 AU Kappa = 2.6579 r_min = 0.314AU alpha = 0.01  period = 0.239
plt.figure(figsize = (16,12))
plt.subplot(111,polar = True)
'''e = 0.2
r_min = 0.314
r_0 = r_min*(1 + e)/(1 - e)
A = solving_ode.ode(0.01,0,30*np.pi,(r_0,0))  
#print 1./(r_min*(1 + e))
A.set_fx(['v','(2.0/r)*v**2+r-'+str(1./(r_min*(1 + e)))+'*(1 + 0.001/(r**2))*r**2'],['t','r','v'])
#A.set_fx(['v','(2.0/r)*v**2+r-2.6579*(1 + 0.01/(r**2))*r**2'],['t','r','v'])
data_record = A.rgkt_4()
theta_record = []'''
#r_0 = 0.47
'''for i in range(len(data_record[1][0]) - 1):
    if ( data_record[1][0][i] > data_record[1][0][i - 1] and data_record[1][0][i] > data_record[1][0][i + 1]):
        theta_record.append(data_record[0][i])
    if ( data_record[1][0][i] < data_record[1][0][i - 1] and data_record[1][0][i] < data_record[1][0][i + 1]):
        print data_record[1][0][i]
print theta_record'''
eccentricities = [0.2,0.5,0.8]
for i in range(3):
    e = eccentricities[i]
    r_min = 0.314
    r_0 = r_min*(1 + e)/(1 - e)
    A = solving_ode.ode(0.01,0,30*np.pi,(r_0,0))  
    A.set_fx(['v','(2.0/r)*v**2+r-'+str(1./(r_min*(1 + e)))+'*(1 + 0.001/(r**2))*r**2'],['t','r','v'])
    data_record = A.rgkt_4()
    plt.plot(data_record[0],data_record[1][0],lw=1,label = 'e = '+str(eccentricities[i]))    
plt.title('Simulation of the precession of Mercury')
plt.legend()
plt.savefig('chapter4_4.11_0.2.png',dpi = 144)
plt.show()


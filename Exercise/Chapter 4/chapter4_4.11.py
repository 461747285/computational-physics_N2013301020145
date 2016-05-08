# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:11:36 2016

@author: AF
"""

import numpy as np
import matplotlib.pyplot as plt
import ode as solving_ode
#from visual import *

###  -------- circular orbit -----------------
e = 0.9
r_min = 0.314
r_0 = r_min*(1 + e)/(1 - e)
a = r_min/(1 - e)
v_0 = np.sqrt(4*np.pi**2*(1 - e)**2/(r_min*(1 + e))) 
A = solving_ode.ode(0.001,0,25,(r_0,0,0,v_0))
A.set_fx(['vx','-4*np.pi**2*x/(np.sqrt(x**2+y**2))**3*(1+0.001/(np.sqrt(x**2+y**2))**2)','vy','-4*np.pi**2*y/(np.sqrt(x**2+y**2))**3*(1+0.001/(np.sqrt(x**2+y**2))**2)'],['t','x','vx','y','vy'])
data_record = A.rgkt_4()
theta_record = []
time_record = []
for i in range(len(data_record[1][0]) - 1):
    if ( data_record[1][0][i]**2+data_record[1][2][i]**2 > data_record[1][0][i - 1]**2+data_record[1][2][i - 1]**2 and data_record[1][0][i]**2+data_record[1][2][i]**2> data_record[1][0][i + 1]**2+data_record[1][2][i + 1]**2):
        time_record.append(data_record[0][i])
        theta_record.append(np.arctan(data_record[1][2][i]/data_record[1][0][i])*180/np.pi)
print time_record
print theta_record

###  ------ vpython -------------------------
'''sun = sphere(pos = (0,0,0),radius = 0.22,color = color.yellow)
lamp = local_light(pos=(0,0,0), color=color.yellow)
deltat = 0.0001
i = 0
t = 0
mercury = sphere(pos = (0.47,0,0), radius = 0.01, material = materials.marble)
mercury.trail = curve(color = color.white)
while i < len(data_record[1][1]):
    rate(300)
    mercury.velocity = vector(data_record[1][1][i], data_record[1][3][i], 0)
    mercury.pos = mercury.pos + mercury.velocity*deltat
    mercury.trail.append(pos = mercury.pos)
    t = t + deltat
    i+=1
'''
### -----------------------------------------
'''plt.figure(figsize = (10,8))
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
#plt.figure(figsize = (16,12))
#plt.subplot(111,polar = True)
'''e = 0.2
r_min = 0.314
r_0 = r_min*(1 + e)/(1 - e)
A = solving_ode.ode(0.01,0,30*np.pi,(r_0,0))  
#print 1./(r_min*(1 + e))
A.set_fx(['v','(2.0/r)*v**2+r-'+str(1./(r_min*(1 + e)))+'*(1 + 0.001/(r**2))*r**2'],['t','r','v'])
#A.set_fx(['v','(2.0/r)*v**2+r-2.6579*(1 + 0.01/(r**2))*r**2'],['t','r','v'])
data_record = A.rgkt_4()
theta_record = []
#r_0 = 0.47
print r_0
for i in range(len(data_record[1][0]) - 1):
    if ( data_record[1][0][i] > data_record[1][0][i - 1] and data_record[1][0][i] > data_record[1][0][i + 1]):
        theta_record.append(data_record[0][i])
    if ( data_record[1][0][i] < data_record[1][0][i - 1] and data_record[1][0][i] < data_record[1][0][i + 1]):
        #print data_record[1][0][i]
        pass
print theta_record'''
'''eccentricities = [0.2,0.5,0.8]
for i in range(3):
    e = eccentricities[i]
    r_min = 0.314
    r_0 = r_min*(1 + e)/(1 - e)
    A = solving_ode.ode(0.01,0,30*np.pi,(r_0,0))  
    A.set_fx(['v','(2.0/r)*v**2+r-'+str(1./(r_min*(1 + e)))+'*(1 + 0.001/(r**2))*r**2'],['t','r','v'])
    data_record = A.rgkt_4()
    plt.plot(data_record[0],data_record[1][0],lw=1,label = 'e = '+str(eccentricities[i]))    
plt.title('Simulation of the precession of Mercury')
plt.legend()'''
plt.savefig('chapter4_4.11.png',dpi = 144)
plt.show()


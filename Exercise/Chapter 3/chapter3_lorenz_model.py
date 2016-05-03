# -*- coding: utf-8 -*-
"""
Created on Tue May  3 22:22:45 2016

@author: AF
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def lorenz(x, y, z, s=10, r=25, b=8.0/3):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
stepCnt = 10000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

'''x_plot = []
y_plot = []
z_plot = []'''

# Setting initial values
xs[0], ys[0], zs[0] = (1.0, 0.0, 0.0)

# Stepping through "time".
for i in range(stepCnt):
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
'''    if xs[i]*xs[i+1]<0.0:
        r = np.abs(xs[i+1]/xs[i])
        y_plot.append((ys[i]*r+ys[i+1])/(1+r))
        z_plot.append((zs[i]*r+zs[i+1])/(1+r)) '''
        

fig = plt.figure(figsize = (8,6))
font = {'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 16}
ax = plt.axes(xlim=(-15, 15), ylim=(0, 35))
line, = ax.plot([], [], 'k.')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    y_plot = []
    z_plot = []
    x_p = i/10.0 - 10.0
    plt.xlabel('y', fontdict=font)
    plt.ylabel('z', fontdict=font)
    for j in range(stepCnt):
        if (xs[j]-x_p)*(xs[j+1]-x_p)<0.0:
            r = np.abs((xs[j+1]-x_p)/(xs[j]-x_p))
            y_plot.append((ys[j]*r+ys[j+1])/(1+r))
            z_plot.append((zs[j]*r+zs[j+1])/(1+r))
    line.set_data(y_plot,z_plot)
    return line,
            
'''y_plot = []
z_plot = []
for j in range(stepCnt):
    if xs[j]*xs[j+1]<0.0:
        r = np.abs(xs[j+1]/xs[j])
        y_plot.append((ys[j]*r+ys[j+1])/(1+r))
        z_plot.append((zs[j]*r+zs[j+1])/(1+r))
plt.scatter(y_plot,z_plot)'''  

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
plt.show()
anim.save('chapter3_butterfly.gif', fps=20, writer='Feng_Chen')
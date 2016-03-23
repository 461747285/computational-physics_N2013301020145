# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:49:37 2016
@author: AF
"""
# this package involve three numerical methods to solve ordinary differential equation.
# they are Euler method, Crome-Euler method and Runge-Kutta method
# reference MATLAB 语言常用算法程序集（第2版）

import matplotlib.pyplot as plt

class ode:
    def __init__(self,f,dx,a,b,Y):
        self.f = f      # the function on the right side 
        self.dx = dx    # step length
        self.a = a      # lower limit
        self.b = b      # upper limit
        self.Y = Y      # initial y
        self.data = [[],[],[],[],[]] # store all the datas
    
    def input_fx(self):                ###input the function on the right side
        self.f = raw_input('please input the expression on the right side (x,y):')
        independent_v = raw_input('please input name of the independent variable of the expression:')
        dependent_v = raw_input('please input the name of the dependent variable of the expression:')
        self.f = self.f.replace(independent_v,'x').replace(dependent_v,'y')
        print self.f
    
    def euler(self):                   ###calculate via Euler method
        self.y = []
        self.x = []
        self.y.append(self.Y)
        self.x.append(self.a)
        self.N = int(float(self.b - self.a)/(self.dx))
        for i in range(1,self.N):
            y = self.y[i - 1]
            x = self.x[i - 1]
            self.y.append(self.y[i - 1] + eval(self.f) * self.dx)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return 0 
        
    def eulerplus(self):                 ### modified euler method
        self.y = []
        self.x = []
        self.y.append(self.Y)
        self.x.append(self.a)
        self.N = int(float(self.b - self.a)/(self.dx))
        for i in range(1,self.N):
            y = self.y[i - 1]
            x = self.x[i - 1]
            v1 = eval(self.f)
            y = self.y[i - 1] + v1*self.dx
            v2 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * (v1 + v2)/2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[2] = self.y
        return 0
        
    def rgkt_2(self):                    ### second order Runge_Kutta
        self.y = []
        self.x = []
        self.y.append(self.Y)
        self.x.append(self.a)
        self.N = int(float(self.b - self.a)/(self.dx))
        for i in range(1,self.N):
            y = self.y[i - 1]
            x = self.x[i - 1]
            v1 = eval(self.f)
            y = self.y[i - 1] + v1*self.dx/2
            x = self.x[i - 1] + self.dx/2
            v2 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * v2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[3] = self.y
        return 0
    
    def rgkt_3(self):                    ### third order Runge_Kutta
        self.y = []
        self.x = []
        self.y.append(self.Y)
        self.x.append(self.a)
        self.N = int(float(self.b - self.a)/(self.dx))
        for i in range(1,self.N):
            y = self.y[i - 1]
            x = self.x[i - 1]
            k1 = eval(self.f)
            x = self.x[i - 1] + self.dx/2
            y = self.y[i - 1] + k1*self.dx/2
            k2 = eval(self.f)
            x = self.x[i - 1] + self.dx
            y = self.y[i - 1] - k1*self.dx + 2*k2*self.dx
            k3 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * (k1 + 4*k2 +k3)/6)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[4] = self.y
        return 0   
    
    def store(self):
        data_file = open('data_ode.txt','w')
        for i in range(self.N):
            for j in range(4):
                data_file.write(str(self.data[j][i]))
                data_file.write(' ')
            data_file.write('\n')
        data_file.close  
    
    def draw_figure(self,j):
        notation = {'1': 'Euler_method','2':'Modified_Euler_method','3':'Second_order_Runge_Kutta method','4':'Third_order_Runge_Kutta method'}
        if (j == 1):
            plt.plot(self.data[0],self.data[j],label = notation[str(j)])
        elif(j == 2):
            plt.plot(self.data[0],self.data[j],label = notation[str(j)])
        elif(j == 3):
            plt.plot(self.data[0],self.data[j],label = notation[str(j)])
        elif(j == 4):
            plt.plot(self.data[0],self.data[j],label = notation[str(j)])
    
A = ode('x',0.05,0,5,100)
A.input_fx()
A.euler()
A.eulerplus()
A.rgkt_2()  
A.rgkt_3()
plt.figure(figsize=(10,6),dpi = 144)
for i in range(4):
    A.draw_figure(i+1)
plt.legend()
plt.savefig('ode.png',dpi=144)  
plt.show()      
        

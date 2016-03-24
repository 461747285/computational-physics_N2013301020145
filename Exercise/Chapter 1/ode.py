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
    def __init__(self,dx,a,b,Y):
        self.dx = dx    # step length
        self.a = a      # lower limit
        self.b = b      # upper limit
        self.Y = Y      # initial y
        self.y = []
        self.x = []
        self.N = int(float(self.b - self.a)/(self.dx))
        self.data = [[],[]] # store all the datas
        
    def set_fx(self,f,independent_v,dependent_v):                ###setting the function on the right side
        self.f = f
        self.number = len(dependent_v)
        self.dep_name = []
        self.dep_name.append(independent_v)
        self.dep_name.append(dependent_v)
        self.dep_name_record = self.dep_name[:]
        return 0    
    
    def set_fxs(self,f,independent_v,dependent_v):                ###setting the function on the right side for equation systems
        self.f = f
        self.number = len(dependent_v)
        self.dep_name = []
        self.dep_name.append(independent_v)
        for i in range(self.number):
            self.dep_name.append(dependent_v[i])
        self.dep_name_record = self.dep_name[:]
        return 0
    
    def euler(self):                   ###calculate via Euler method
        if (self.number != 1):
            print 'this method cannot solve ode equation systems.'
            exit()
        self.y.append(self.Y)
        self.x.append(self.a)
        for i in range(1,self.N):
            self.dep_name[1] = self.y[i - 1]
            self.dep_name[0] = self.x[i - 1]
            self.y.append(self.y[i - 1] + eval(self.f) * self.dx)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
        
    def eulerplus(self):                 ### modified euler method
        if (self.number != 1):
            print 'this method cannot solve ode equation systems.'
            exit()
        self.y.append(self.Y)
        self.x.append(self.a)
        for i in range(1,self.N):
            self.dep_name[1] = self.y[i - 1]
            self.dep_name[0] = self.x[i - 1]
            v1 = eval(self.f)
            self.dep_name[1] = self.y[i - 1] + v1*self.dx
            v2 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * (v1 + v2)/2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
        
    def rgkt_2(self):                    ### second order Runge_Kutta
        if (self.number != 1):
            print 'this method cannot solve ode equation systems.'
            exit()
        self.y.append(self.Y)
        self.x.append(self.a)
        for i in range(1,self.N):
            self.dep_name[1] = self.y[i - 1]
            self.dep_name[0] = self.x[i - 1]
            v1 = eval(self.f)
            self.dep_name[1] = self.y[i - 1] + v1*self.dx/2
            self.dep_name[0] = self.x[i - 1] + self.dx/2
            v2 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * v2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
    
    def rgkt_3(self):                    ### third order Runge_Kutta
        if (self.number != 1):
            print 'this method cannot solve ode equation systems.'
            exit()
        self.y.append(self.Y)
        self.x.append(self.a)
        for i in range(1,self.N):
            self.dep_name[1] = self.y[i - 1]
            self.dep_name[0] = self.x[i - 1]
            k1 = eval(self.f)
            self.dep_name[0] = self.x[i - 1] + self.dx/2
            self.dep_name[1] = self.y[i - 1] + k1*self.dx/2
            k2 = eval(self.f)
            self.dep_name[0] = self.x[i - 1] + self.dx
            self.dep_name[1] = self.y[i - 1] - k1*self.dx + 2*k2*self.dx
            k3 = eval(self.f)
            self.y.append(self.y[i - 1] + self.dx * (k1 + 4*k2 +k3)/6)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data  
        
    def eulers(self):                   ###calculate equations via Euler method
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial valye
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for j in range(self.number):
                for k in range(self.number):
                    self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1])
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
                for m in range(self.number + 1):
                    exec self.dep_name[m]
                self.y[j].append(self.y[j][i - 1] + eval(self.f[j]) * self.dx)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
        
    def rgkt_3s(self):                  ### third order Runge_Kutta for equation systems
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial valye
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for j in range(self.number):
                for d in range(self.number):
                    self.dep_name[d + 1] = self.dep_name_record[d + 1] + '=' + str(self.y[d][i - 1])
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
                for m in range(self.number + 1):
                    exec self.dep_name[m]
                k1 = eval(self.f[j])
                for e in range(self.number):
                    self.dep_name[e + 1] = self.dep_name_record[e + 1] + '=' + str(self.y[e][i - 1] + k1*self.dx/2)
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1]+self.dx/2)
                for n in range(self.number + 1):
                    exec self.dep_name[n]
                k2 = eval(self.f[j])
                for f in range(self.number):
                    self.dep_name[f + 1] = self.dep_name_record[f + 1] + '=' + str(self.y[f][i - 1] - k1*self.dx + 2*k2*self.dx)
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx)
                for o in range(self.number + 1):
                    exec self.dep_name[o]
                k3 = eval(self.f[j])
                self.y[j].append(self.y[j][i - 1] + self.dx * (k1 + 4*k2 +k3)/6)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data 
    
    def store(self):
        data_file = open('data_ode.txt','w')
        for i in range(self.N):
            data_file.write(str(self.data[0][i]))
            data_file.write(' ')
            for j in range(len(self.data[1])):
                data_file.write(str(self.data[1][j][i]))
                data_file.write(' ')
            data_file.write('\n')
        data_file.close  
    
    
A = ode(0.05,0,5,(100,0))
A.set_fxs(['y2-y1','y1-y2'],'x',('y1','y2'))
#A.euler()
#A.eulerplus()
#A.rgkt_2()  
#A.rgkt_3()
#plt.figure(figsize=(10,6),dpi = 144)
record = []
record = A.rgkt_3s()
A.store()
plt.plot(record[0],record[1][0], label ='particle a')
plt.plot(record[0],record[1][1], label ='particle b')
plt.legend()
plt.savefig('ode.png',dpi=144)  
plt.show()      
        

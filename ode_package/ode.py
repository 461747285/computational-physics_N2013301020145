# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:49:37 2016
@author: AF
version 3.1
"""
# this package involve three numerical methods to solve ordinary differential equation.
# they are Euler method, Crome-Euler method and Runge-Kutta method
# reference MATLAB 语言常用算法程序集（第2版）

import math
import numpy

class ode:
    def __init__(self,dx,a,b,Y):
        self.dx = dx    # step length
        self.a = a      # lower limit
        self.Y = [0]
        if (type(Y) == int):
            self.Y[0] =Y
        else:
            self.Y = Y      # initial y
        self.N = int(float(b - self.a)/(self.dx))
        self.data = [[],[]] # store all the datas
           
    def set_fx(self,f,variable_name):                ###setting the function on the right side 
        self.f = [0]
        if (type(f) == str):
            self.f[0] = f
        else:
            self.f = f
        self.number = len(variable_name) - 1
        self.dep_name = []
        for i in range(len(variable_name)):
            self.dep_name.append(variable_name[i])
        self.dep_name_record = self.dep_name[:]
        return 0
        
    def euler(self):                   ###simple Euler method
        self.y = []
        self.x = []
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
        
    def eulerplus(self):                 ### modified euler method 
        self.y = []
        self.x = []
        self.x.append(self.a)
        for l in range(self.number):    ##
            self.y.append([])           ####   setting the initial valye
            self.y[l].append(self.Y[l]) ##
        for i in range(1,self.N):
            for j in range(self.number):
                for k in range(self.number):
                    self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1])
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
                for m in range(self.number + 1):
                    exec self.dep_name[m]
                v1 = eval(self.f)
                self.dep_name[j + 1] = self.dep_name_record[j + 1] + '=' + str(self.y[j][i - 1] + v1*self.dx)
                exec self.dep_name[j + 1]
                v2 = eval(self.f)
                self.y[j].append(self.y[j][i - 1] + self.dx * (v1 + v2)/2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
        
    def rgkt_2(self):                    ### second order Runge_Kutta
        self.y = []
        self.x = []
        self.x.append(self.a)
        for l in range(self.number):    ##
            self.y.append([])           ####   setting the initial valye
            self.y[l].append(self.Y[l]) ##
        for i in range(1,self.N):
            for j in range(self.number):
                for k in range(self.number):
                    self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1])
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
                for m in range(self.number + 1):
                    exec self.dep_name[m]
                v1 = eval(self.f)
                self.dep_name[j + 1] = self.dep_name_record[j + 1] + '=' + str(self.y[j][i - 1] + v1*self.dx/2)
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
                exec self.dep_name[0]
                exec self.dep_name[j + 1]
                v2 = eval(self.f)
                self.y[j].append(self.y[j][i - 1] + self.dx * v2)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] =self.x
        self.data[1] =self.y
        return self.data
        
    def rgkt_3(self):                  ### third order Runge_Kutta 
        self.y = []
        self.x = []
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
                self.dep_name[j + 1] = self.dep_name_record[j + 1] + '=' + str(self.y[j][i - 1] + k1*self.dx/2)
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1]+self.dx/2)
                exec self.dep_name[0]
                exec self.dep_name[j + 1]
                k2 = eval(self.f[j])
                self.dep_name[j + 1] = self.dep_name_record[j + 1] + '=' + str(self.y[j][i - 1] - k1*self.dx + 2*k2*self.dx)
                self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx)
                exec self.dep_name[0]
                exec self.dep_name[j + 1]
                k3 = eval(self.f[j])
                self.y[j].append(self.y[j][i - 1] + self.dx * (k1 + 4*k2 +k3)/6)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data 
 
    def store(self,data__file):           #### save the calculculate datas            
        data_file = open(data__file,'w')
        for i in range(self.N):
            data_file.write(str(self.data[0][i]))
            data_file.write(' ')
            if (len(self.data[1] == 1)):
               data_file.write(str(self.data[1][i]))
            else:
                for j in range(len(self.data[1])):
                    data_file.write(str(self.data[1][j][i]))
                    data_file.write(' ')
            data_file.write('\n')
        data_file.close  


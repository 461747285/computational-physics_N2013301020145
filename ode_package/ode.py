# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:49:37 2016
@author: AF
version 4.0
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
    
    def Exe(self,string):
        pass
        
    def euler(self):                   ###simple Euler method
        self.y = []
        self.x = []
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial value
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1])
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                self.y[j].append(self.y[j][i - 1] + eval(self.f[j]) * self.dx)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data
        
    def rgkt_2(self):                    ### second-order Runge_Kutta
        self.y = []
        self.x = []
        v1 = [0]*self.number
        v2 = [0]*self.number
        self.x.append(self.a)
        for l in range(self.number):    ##
            self.y.append([])           ####   setting the initial value
            self.y[l].append(self.Y[l]) ##
        print self.number
        for i in range(1,self.N):
            for n in range(self.number):
                self.dep_name[n + 1] = self.dep_name_record[n + 1] + '=' + str(self.y[n][i - 1])
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                v1[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] + v1[k]*self.dx/2)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                v2[j] = eval(self.f[j])
            for k in range(self.number):
                self.y[k].append(self.y[k][i - 1] + self.dx * v2[k])
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] =self.x
        self.data[1] =self.y
        return self.data
        
    def rgkt_3(self):                  ### third-order Runge_Kutta 
        self.y = []
        self.x = []
        k1 = [0]*self.number
        k2 = [0]*self.number
        k3 = [0]*self.number
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial value
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for d in range(self.number):
                self.dep_name[d + 1] = self.dep_name_record[d + 1] + '=' + str(self.y[d][i - 1])
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k1[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] + k1[k]*self.dx/2)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k2[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] - k1[k]*self.dx + 2*k2[k]*self.dx)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k3[j] = eval(self.f[j])
            for k in range(self.number):
                self.y[k].append(self.y[k][i - 1] + self.dx * (k1[k] + 4*k2[k] +k3[k])/6)
            self.x.append(self.x[i - 1] + self.dx)
        self.data[0] = self.x
        self.data[1] = self.y
        return self.data 
 
    def rgkt_4(self):                  ### forth-order Runge_Kutta 
        self.y = []
        self.x = []
        k1 = [0]*self.number
        k2 = [0]*self.number
        k3 = [0]*self.number
        k4 = [0]*self.number
        self.x.append(self.a)           #
        for l in range(self.number):    ###
            self.y.append([])           ####    setting the initial value
            self.y[l].append(self.Y[l]) ###
        for i in range(1,self.N):
            for d in range(self.number):
                self.dep_name[d + 1] = self.dep_name_record[d + 1] + '=' + str(self.y[d][i - 1])
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1])
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k1[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] + 0.5*k1[k]*self.dx)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k2[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] + 0.5*k2[k]*self.dx)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx/2)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k3[j] = eval(self.f[j])
            for k in range(self.number):
                self.dep_name[k + 1] = self.dep_name_record[k + 1] + '=' + str(self.y[k][i - 1] + k3[k]*self.dx)
            self.dep_name[0] = self.dep_name_record[0] + '=' + str(self.x[i - 1] + self.dx)
            for m in range(self.number + 1):
                exec self.dep_name[m]
            for j in range(self.number):
                k4[j] = eval(self.f[j])
            for k in range(self.number):
                self.y[k].append(self.y[k][i - 1] + self.dx * (k1[k] + 2*k2[k] + 2*k3[k] + k4[k])/6)
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


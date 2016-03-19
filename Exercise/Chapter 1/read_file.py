# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:59:27 2016
@author: AF
"""

import matplotlib.pyplot as plt


def read_initial(initial_file):
    itxt= open(initial_file)
    initial_data=[]
    data =[]  
    for lines in itxt.readlines():
        lines=lines.replace("\n","").split(",")
        initial_data.append(lines)
    print len(initial_data[0][0].split(' '))
    for i in range(len(initial_data[0][0].split(' '))):
        data.append([])
        for j in range(len(initial_data)):
            data[i].append(initial_data[j][0].split(' ')[i])
    itxt.close()
    return data     ### data[0] = x, data[1] = y1, data[2] = y2,...
    
def draw_figure(data):
    for i in range(1,len(data)):
        plt.plot(data[0],data[i])
    plt.xlabel('time(s)')
    plt.ylabel('Number of Nuclei')
#    plt.text(3,0.8*y[0],'Time Constant ='+str(tc)+'s'+'\n'+'Time Step ='+str(dt)+'s')
    plt.show()

def main():
    data = read_initial('data.txt')
    print data
    draw_figure(data)

main()      



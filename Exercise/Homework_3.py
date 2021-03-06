# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:59:27 2016
@author: AF
"""
import os
import math
import time

def read_initial(initial_file):           ######## read the initial.txt and transfer it into a 2d list
    itxt= open(initial_file)
    initial_screen=[]
    for lines in itxt.readlines():
        lines=lines.replace("\n","").split(",")
        initial_screen.append(lines)
    itxt.close()
    for i in range(len(initial_screen)):
        initial_screen[i].extend(initial_screen[i][0])
        del initial_screen[i][0]
    return initial_screen
    
def rotation(angle,xscreen,l2,s,x_):
    if (angle != 0):
        for j in range(l2):
            if (xscreen[x_][j] == s):
                radius = j - 60
                x = int(radius*math.cos(angle*math.pi/180))+60
                y = int(radius*math.sin(angle*math.pi/180))+x_
                xscreen[y][x] = xscreen[x_][j]
                xscreen[x_][j] = ' '
            else:
                pass
        return xscreen
    else:
        return xscreen 

def output_screen(l,w,oscreen):
    final_screen = [' ']*(w-1)
    for i in range(w-1):
        for j in range(l-1):
            final_screen[i] = final_screen[i]+oscreen[i][j]
        print final_screen[i]
    print '\n' 
    
def main():
    while True:
        hours = time.localtime(time.time())[3]
        if (hours >=12):
            hours = hours - 12
        minutes = time.localtime(time.time())[4]
        seconds = time.localtime(time.time())[5]
        iscreen = read_initial('initial.txt')
        length = len(iscreen[0])
        width = len(iscreen)
        fscreen = rotation(((hours+minutes/60)*30)-90,rotation((minutes*6)-90,rotation((seconds*6)-90,iscreen,length,'^',23),length,'*',22),length,'$',21)
        output_screen(length,width,fscreen)
        time.sleep(0.5)
        os.system('clear')

main()

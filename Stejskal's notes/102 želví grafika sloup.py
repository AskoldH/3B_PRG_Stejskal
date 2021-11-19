# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:05:29 2012

@author: Martin
"""
"""
pensize(x)- nastaví tloušťku čáry
"""
from turtle import *

def Sloup(x,y):
    if x>5:
        pensize(y)
        forward(x)
        right(20)
        Sloup(x/2,y-1)
        left(20)
        back(x)


up()
left(90)
goto(0,-250)
down()
speed(1)

Sloup(250,8)
exitonclick()
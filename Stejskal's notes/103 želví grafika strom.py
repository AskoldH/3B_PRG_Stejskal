# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 07:52:12 2012

@author: Martin
"""
from turtle import *

uhel=40

def strom(x,t):
    if x>2:
        pensize(t)
        forward(x)
        right(uhel)
        strom(x/2,t-1)
        right(uhel)
        strom(x/2,t-1)
        left(3*uhel)
        strom(x/2,t-1)
        right(uhel)
        back(x)

up()
left(90)
goto(0,-250)
down()
speed(0)

strom(300,8)
exitonclick()
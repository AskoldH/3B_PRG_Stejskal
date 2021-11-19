# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 08:39:24 2012

@author: Martin
"""

from turtle import *
delka=200

def zub(x=100):
    if x>20:
        zub(x/3)
        right(60)
        zub(x/3)
        left(120)
        zub(x/3)
        right(60)
        zub(x/3)
    else:
        forward(x)

speed(0)
zub(delka)
left(120)
zub(delka)
left(120)
zub(delka)
exitonclick()
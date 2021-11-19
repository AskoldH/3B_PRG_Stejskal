# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 09:22:55 2012

@author: Martin
"""

def fib(x):
    if x==1:
        return(0)
    elif x==2:
        return(1)
    else:
        return(fib(x-1)+fib(x-2))
        
print fib(30)        
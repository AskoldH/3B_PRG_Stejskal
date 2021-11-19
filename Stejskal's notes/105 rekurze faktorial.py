# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 09:03:38 2012

@author: Martin
"""

def faktorial(x):
    if x==1:
        return(1)
    else:
        return(x*faktorial(x-1))
        
print faktorial(5)        
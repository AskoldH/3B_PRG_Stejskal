# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:17:28 2012

@author: Martin
"""
"""
fill_between(x,y1,y2) - vyplní plochu mezi dvěma čarami, druhá je
                        nepovinná
                      - lze doplnit o podmínku   
"""

from pylab import *

x=arange(0,2*pi,0.1)
y1=cos(x)
y2=sin(x)
#y2=x/3

#plot(x,y1)
plot(x,y2)
fill_between(x,y2,facecolor="yellow",where=(y2>0)*(x<2))
show()


#plot(x,y1)
#plot(x,y2)
#fill_between(x,y1,y2,where=(y2<0),facecolor="b")
#show()
#
#plot(x,y1)
#plot(x,y2)
#fill_between(x,y1,y2,where=(y2>=0)*(x<=1),facecolor="g")
#
#grid()
show()

"""
Úkol:
1) Vyplňte plochu mezi fcemi cos(x) a sin(2*x) fialovou 
   barvou v hexadecimálním tvaru na intervalu <0,2*pi>.
"""   
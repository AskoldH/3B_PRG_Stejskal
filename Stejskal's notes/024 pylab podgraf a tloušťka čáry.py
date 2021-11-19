# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:34:21 2012

@author: Martin
"""
"""
subplot(x,y,z) - specifikuje, do kterého grafu v aktuálním obrázku se
                 bude kreslit (x=pocet řádků, y=pocet sloupců, z=číslo
                 grafu)
               - rozložení x a y musí být stejné  
"""

from pylab import *

subplot(2,2,1)
plot([1,2,3,5], linewidth=4)
plot([3,1,5,2])

subplot(2,2,2)
plot([3,2,6,2])

subplot(2,2,3)
plot([1,2,3,5],"y--", linewidth=4)
plot([3,1,5,2])

subplot(2,2,4)
plot([3,2,6,2])


show()



"""
Úkol:
1) Zabrazte fci y=|x-1|+1 ve dvou grafech pod sebou, 
   pokaždé jinou barvou.
   Použijte funkci abs().
"""

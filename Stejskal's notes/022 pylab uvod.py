# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:35:52 2012

@author: Martin
"""
"""
Materiály:
http://matplotlib.org/
http://mamut.spseol.cz/matplotlib/    
    
"""    

from pylab import *
x=arange(-5,5,0.2) #vektor x od -10 do 10, krok 0.2
print(x)

x=linspace(-5,5,30) #vektor x od -10 do 10, 100 hodnot
#print(x)

y1=2*x+1
y2=x**2
#y3=x**3
#
grid() #zobrazení mřížky
title("Graf funkce x3")
xlabel("Osa x") # popis osy x
ylabel("Osa y")
#
plot(x,y1,label="$y=2x+1$") #vložení údajů do grafu
plot(x,y2,label="$y=\sqrt{x^2}$") #syntaxe jazyka latex
#plot(x,y3,label="$y=x^4$")
ylim(-1,10) #limity pro osu y
xlim(-3,3)
legend(loc="upper center") #zobrazení legendy umístění řetězcem nebo číslem 0-10
show()


x=[0,1,-1,3,4]
y=[5,2,1,2,-1]
plot(x,y)
show() #zobrazení grafu a anulování všech nastavení


"""
Úkol:
0) Zobrazte graf funkce y=1/x, kde x patří do <1,10>
1) Zobrazte graf funkce y=cos(x), interval  <0,4*pi>
2) Vypočítejte hodnoty funkce y1=2cos(3x)-1 a 
   přidejte ji do grafu
3) Vytvořte si seznam 10-ti náhodných x-vých hodnot
   a obdobný seznam y-vých hodnot. Zobrazte graf. 
"""   

"""
Opakovací
0) Zobrazte graf funkce y=odmocnina(x), kde x patří do <0,1000>
"""
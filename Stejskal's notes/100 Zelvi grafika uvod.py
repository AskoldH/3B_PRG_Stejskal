# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:07:43 2012

@author: Martin
"""
"""
Operace:
    shape() - volba tvaru želvy
    speed() - rychlost želvy (1=pomalu, 10=rychle)
    forward() - posun dopředu o daný počet bodů
    back() - analogicky
    left() - otočení doleva o daný úhel
    right() - analogicky
    up() - želva nekreslí
    down() - želva kreslí

    dot() - nakreslí tečku
    stamp() - zanechá obrázek želvy
    goto(x,y) - přejde přímo na dané souřadnice
    xcor() - vrací x-ovou souřadnici želvy
    ycor() - vrací y-ovou souřadnici želvy
    exitonclick() - uzavření okna po kliknutí myší
"""    

from turtle import *

shape("turtle")
speed(1)

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
exitonclick()

"""
Úkoly:
1) Zkuste nakreslit obálku nebo domek.
"""    
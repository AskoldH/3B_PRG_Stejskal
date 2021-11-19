# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 12:04:24 2013

@author: Radek
"""
"""
Canvas

"""
from tkinter import *
from random import *

hlavni = Tk()

w = Canvas(hlavni,width=300, height=150)
w.pack()

def Zmena(udalost):
    barvy=["red","green","blue","brown","orange","yellow","white","gray"]
    w.itemconfig(obdelnik,fill=barvy[randint(0,len(barvy)-1)])
    w.move(obdelnik,20,20)
    w.coords(obdelnik, 10,10,40,30)
    w.delete(3)
  
elipsa=w.create_oval(0,0,100,50,fill="green",outline="orange")  
cara1=w.create_line(0, 0, 200, 100,fill="yellow")
cara2=w.create_line(0, 100, 200, 0, fill="red", dash=(20, 4))
obdelnik=w.create_rectangle(50, 25, 150, 75, fill="blue")

print (elipsa, cara1, cara2, obdelnik)

w.bind("<1>",Zmena)

mainloop()


"""
Úkol:
1)Nakreslete 5 úseček s náhodnými souřadnicemi.
  Pomocí cyklu!
  Vylepšení: úsečky budou po nějakém čase měnit pozici
2)Pomocí událostí naprogramujte nakreslení obdélníku.
  (někam kliknu a táhnu myší)
""" 




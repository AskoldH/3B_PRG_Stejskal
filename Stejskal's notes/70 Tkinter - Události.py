# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 10:00:12 2013

@author: Radek
"""

from tkinter import *

hlavni = Tk()

def LevyKlik(udalost):
    print ("Klikl jsi na frame na pozici:", udalost.x, udalost.y)

def Najeti(udalost):
    print ("Najel jsi na frame")
#    print udalost

def Klavesa(udalost):
    print ("Stiskl jsi ", udalost.char)
#    print (udalost)

def Pohyb(udalost):
    print (udalost.x, udalost.y)

def F1(udalost):
    print ("Stiskl jsi F1")
    
vstup = Entry(hlavni)
vstup.bind("<Key>", Klavesa)
vstup.bind("<F1>",F1)
vstup.pack()
  
ramec = Frame(hlavni, width=100, height=100,bg="red")
ramec.bind("<Button-1>", LevyKlik)
ramec.bind("<Enter>", Najeti)
ramec.bind("<B1-Motion>",Pohyb)
ramec.pack()

hlavni.mainloop()

"""
1) Vložte do hl. okna frame, který bude reagovat na
   pravé tlačítko myši a vždy si nastaví náhodnou
   barvu pozadí.
2) Při stisku levého tlačítka se nastaví bílé pozadí.
3) Vytvořte program s jedním tlačítkem, které se po
   najetí myši přesune na náhodné místo v okně.
"""   
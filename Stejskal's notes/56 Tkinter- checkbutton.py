# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:06:38 2012

@author: Radek
"""
from tkinter import * 


hlavni = Tk()
v = IntVar() #BooleanVar()
v.set(1)

c = Checkbutton(hlavni, text="Přepínač", variable=v) 
c.grid(row=0,column=1) 

def tisk():
    print (v.get())    
    
tlacitko=Button(hlavni,text="Kontrola",command=tisk)
tlacitko.grid(row=0,column=0)
 
mainloop() 
"""
Úkol:
1) Vložte do okna 2 zaškrtávací políčka a tlačítko
   "Inverze", které invertuje u obou políček jejich
   nastavení.
   Nápověda: Využijeme operaci v.set()
"""   

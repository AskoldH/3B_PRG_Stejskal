# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:24:32 2013

@author: Radek
"""
from tkinter import *

hlavni=Tk()

t=StringVar()

vstup=Entry(hlavni,textvariable=t)
vstup.pack()

vstup2=Entry(hlavni,textvariable=t, state="disabled")
vstup2.pack()


def Nastav():
     t.set("Pokusný text")
     print(t.get())

tlacitko=Button(hlavni,text="Vlož text",command=Nastav)
tlacitko.pack()

mainloop()  
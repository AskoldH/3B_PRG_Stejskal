# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:26:22 2013

@author: Radek
"""

from tkinter import *
from tkinter import messagebox

hl_okno=Tk()          # toto vytvoří hlavní okno

sez=[]

def ObsluhaTlacitka(x):
    messagebox.showinfo("Obsluha","Klikl jsi na tlačítko "+str(x))

for i in range(20):
    txt=StringVar()
    txt.set("Tlačítko "+str(i))
    b=Button(hl_okno,textvariable=txt,command=lambda x=i:ObsluhaTlacitka(x))
    sez.append(b)
    b.pack(fill=X)   

sez[13]["state"]=DISABLED

hl_okno.mainloop()


"""
Úkol:
0) Vykreslete tabulku 4x4 z komponent Entry.
1) Pomocí obdobného mechanismu vykreslete tabulku
   o 5-ti sloupcích a 10-ti řádcích složenou z komponent
   Entry + zmenšete šířku. Použijte rozmístění Grid.
2) Vložte do každého políčka jeho souřadnice.
3) Obarvěte políčka v každém řádku náhodnou barvou.
"""    








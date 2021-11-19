# -*- coding: utf-8 -*-
"""
Created on Tue Dec 04 10:47:54 2012

@author: Radek
"""

from tkinter import *

hl_okno=Tk()          # toto vytvoří hlavní okno

jmeno=Label(hl_okno, text="Zadej jméno:")
jmeno.grid(row=0,sticky=W)         
prijmeni=Label(hl_okno, text="Zadej příjmení:")
prijmeni.grid(row=1,sticky=E)  
vstup1=Entry(hl_okno)
vstup1.grid(row=0,column=1)         
vstup2=Entry(hl_okno)
vstup2.grid(row=1,column=1)         



kontrola=Label(hl_okno,text="")
kontrola.grid(row=2,columnspan=2)

def Zkontroluj():
    ret1=vstup1.get()
    ret2=vstup2.get()
    ret3=ret1+" "+ret2
    kontrola["text"]=ret3

tlacitko1=Button(hl_okno,text="Kontrola",command=Zkontroluj)
tlacitko1.grid(row=3)
tlacitko2=Button(hl_okno,text="Kontrola",command=Zkontroluj)
tlacitko2.grid(row=4,sticky=W+E)

tlacitko3=Button(hl_okno,text="Konec",command=hl_okno.destroy)
tlacitko3.grid(row=3,column=1,rowspan=2, sticky=W+E+N+S)

hl_okno.mainloop() 


"""
Úkol:
1) Rozmístěte tlačítka a ostatní komponenty jako na
   kalkulačce pomocí rozmístění GRID 
   (P:\stejskal\Python\Cvičení Tkinter\cv2 - grid.jpg).
"""      

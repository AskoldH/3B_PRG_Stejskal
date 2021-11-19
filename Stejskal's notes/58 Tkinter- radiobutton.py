# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:44:14 2012

@author: Radek
"""

from tkinter import * 

hlavni = Tk()
ramecek=Frame(hlavni,bd=2,relief="ridge")
ramecek.grid(row=0)

v = IntVar() 
v.set(0)

def tisk():
    print (v.get())

def nastav():
    v.set(2)
    
r1=Radiobutton(ramecek, text="Jedna", variable=v, value=1)
r1.grid(row=0,sticky=W) 
r2=Radiobutton(ramecek, text="Dva", variable=v, value=2,command=tisk)
r2.grid(row=1,sticky=W)
r3=Radiobutton(ramecek, text="Tri", variable=v, value=3) 
r3.grid(row=2,sticky=W) 

    
tlacitko=Button(hlavni,text="Kontrola",command=tisk)
tlacitko.grid(row=1)
tlacitko2=Button(hlavni,text="Nastav",command=nastav)
tlacitko2.grid(row=2)
 
mainloop() 

"""
1) Vytvořte skupinu tří radiobuttonů s různými pozdravy.
   Přidejte tlačítko 'Pozdrav'. Po jeho stisku se 
   zobrazí hláška s daným pozdravem (použijte showinfo).
"""   
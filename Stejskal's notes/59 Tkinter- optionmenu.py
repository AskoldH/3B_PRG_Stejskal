# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:24:22 2012

@author: Radek
"""

from tkinter import *

okno = Tk()
okno["bg"]="red"

promenna = StringVar()
promenna.set("jedna") # standardní hodnota

def test(hodnota):
    print ("hodnota je:", hodnota)
    print ("hodnota je:", promenna.get())

sez=["jedna", "dva", "tři","čtyři"]
w = OptionMenu(okno, promenna,*sez,command=test)
w.pack(side="left")

mainloop()


"""
1) Vytvořte rozbalovací nabídku s třemi barvami a při
   výběru nastavte danou barvu na pozadí okna.

   Zkuste použít slovník:
   barvy={"červená":"#ff0000","bílá":"#ffffff"}
   okno["bg"]=barvy[promenna.get()]
"""   







# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:35:00 2013

@author: Radek
"""
from tkinter import colorchooser
from tkinter import *


hlavni=Tk()

barva=colorchooser.askcolor(title="Barva")
print (barva)
#print (barva[0])
#print (barva[1])
hlavni["bg"]=barva[1]


mainloop()

"""
Úkol:
1) Do aplikace vložte tlačítko pro výběr barvy.
   Výběr barvy proveďte pomocí barevného dialogu.
   Vybranou barvu nastavte na pozadí tlačítka.
"""   
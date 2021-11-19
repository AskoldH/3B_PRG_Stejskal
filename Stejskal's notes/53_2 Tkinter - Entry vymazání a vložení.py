# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:17:56 2012

@author: Radek
"""

"""
Parametry:
    state="readonly"/"disabled"/"normal" - čtení/nepřístupný
"""

from tkinter import *

hlavni=Tk()

vstup=Entry(hlavni,state="normal")
vstup.pack()

def Smaz():
#     vstup.delete(0,END)
    vstup["state"]="disabled"
    tlacitko["state"]="disabled"
#     vstup.insert(0,"Prázdný text")

tlacitko=Button(hlavni,text="Smazani",command=Smaz)
tlacitko.pack()

mainloop()  
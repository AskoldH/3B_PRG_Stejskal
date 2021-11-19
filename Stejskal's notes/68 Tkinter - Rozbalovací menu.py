# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:35:54 2013

@author: Radek
"""


from tkinter import *
from tkinter import messagebox
hlavni = Tk()

#vytvoření hlavního menu
HorniMenu=Menu(hlavni)

def Soubor():
    messagebox.showinfo("Soubor","Tato část není naprogramována!")
  
#vytvoření jedné rozbalovací nabídky a připojení do hl. menu 
MenuSoubor=Menu(HorniMenu,tearoff=0)
MenuSoubor.add_command(label="Otevřít",command=Soubor)
MenuSoubor.add_command(label="Uložit",command=Soubor)
MenuSoubor.add_separator()
MenuSoubor.add_command(label="Konec",command=hlavni.destroy)

HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)

#zobrazení hlavního menu
hlavni.config(menu=HorniMenu)

mainloop()

"""
Úkol:
1) Vytvořte program ukázky jazyků s rozbalovacím menu
   o dvou položkách:

   Soubor
    - Anglicky
    - Německy
    - Španělsky
    - Konec
    
   Nápověda
    - O aplikaci
    - O autorovi
   
"""    
    
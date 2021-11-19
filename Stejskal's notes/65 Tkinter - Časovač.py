# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 09:54:43 2013

@author: Radek
"""
"""
Funkce after
- jedná se o časové zpoždění v milisekundách
- je to funkce hlavního okna, volá se tedy hl.after(...)
- po jeho uplynutí času se buď nestane nic (např. hl.after(1000))
- nebo se spustí požadovaná funkce (např. hl.after(1000,funkce))
"""

from tkinter import messagebox
from tkinter import *


hlavni=Tk()
"""
def Okno():
    messagebox.showinfo("Hlášení","Proběhne prodleva 5000 ms") 
    hlavni.after(5000)
    messagebox.showinfo("Hlášení","Proběl časový interval 5000 ms") 

tlacitko=Button(hlavni,text="Test časovače",command=Okno)
tlacitko.pack()
"""

#pocet=0
#def Vypis():
#   global pocet
#   if pocet<10:    
#        print ("Proběhl vypis")
#        hlavni.after(1000,Vypis)
#        pocet+=1
#Vypis()

import random
barvy=["red","green","blue","white","yellow","orange","grey","brown"]
def ZmenBarvu():
    hlavni["bg"]=random.choice(barvy)
    hlavni.after(100,ZmenBarvu)

ZmenBarvu()



mainloop()

"""
Úkol:
1) Každou sekundu změňte barevné pozadí hlavního okna.
2) Naprogramujte nastavitelný timer, použijte Spinbox.   
"""
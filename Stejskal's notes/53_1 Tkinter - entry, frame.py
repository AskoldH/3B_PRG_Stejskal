# -*- coding: utf-8 -*-

from tkinter import *


hlavni = Tk()
hlavni.title("Výpočet 2. mocniny")

ramecek=Frame(hlavni, bd=1, relief="sunken")
ramecek.pack()

vstup=Entry(ramecek, width=25)
vstup.pack(side="left",padx=10, pady=10)

napis=Label(ramecek,text="0",font=("Arial",50))
napis.pack(side="left")

def vypocet():
    x=int(vstup.get())
    napis["text"]=str(x**2)
   
tlacitko=Button(ramecek, text= u"Druhá mocnina", command=vypocet)
tlacitko.pack(side="left", padx=10, pady=10)

hlavni.mainloop()

"""
Úkol:
1) Vložte do okna jeden Frame a do něj Label, jedno Entry a 
   Button tak, aby byly vedle sebe.
   Při stisku tlačítka se text z Entry předá do Labelu.
    
2) Napište aplikaci, která bude obsahovat:
   - Label "Tajná šifra" - zvětšené písmo
   - Entry pro vstup textu
   - Tlačítko "Šifruj vstup"
   - Label pro výstup
   - Tlačítko "Konec"
   - vhodně použijte Frame
   
   Po stisku tlačítka se řetězec ze vstupu zašifruje 
   libovolnou metodou a výsledek se zobrazí v labelu.
"""    
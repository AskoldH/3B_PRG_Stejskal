# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 11:31:49 2013

@author: Radek
"""
"""
Komponenta Text
---------------
metoda tag_config(název, font=, foreground=, underline=)
- definice stylu

metoda insert(řádek.pozice, řetězec, styl)
- vkládá do textového pole řetězec na zadaný řádek od dané pozice
- ano, tyto dva údaje se oddělují tečkou
- pokud daná pozice neexistuje, vkládá na konec textu
- vložený text je formátován zvoleným stylem

metoda delete(...)
- smázání vymezené části textu
"""

from tkinter import *

hlavni=Tk()
text=Text(hlavni)
text.pack(fill=BOTH, expand=1)

text.tag_config("modry", font="Arial 20 italic", foreground="blue", underline=1)
text.tag_config("cerveny", font="Arial 15 bold", foreground="red", underline=0)

text.insert(1.0,"Ahoj studenti!\n","modry")
text.insert(5.0, "Jak se máte?\n","cerveny")
text.insert(END, "To je dnes hezky...")


smazat=Button(hlavni,text="Smazat vše", command=lambda: text.delete(1.0, END))
smazat.pack()

retezec=text.get(1.0,END)
print (retezec)

mainloop() 

"""
Úkol:
1) Vytvořte jednoduchý textový editor, který umožní
   uložit nebo načíst obsah komponenty text ze souboru.
   Vše bez formátování = bez použití stylů.
   Použijte souborové dialogy.
"""    
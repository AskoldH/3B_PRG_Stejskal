# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:59:59 2013

@author: Radek
"""

from tkinter import *
from tkinter import messagebox

okno = Tk()

group = LabelFrame(okno, text="Zadej kladné číslo", padx=10, pady=10)
group.pack(padx=10, pady=10)

def kontrola():
    try:
        cislo=int(w.get())
        if cislo<0:
            messagebox.showwarning("Výstraha","Pozor, číslo nesmí být záporné!")
            w.delete(0,END)            
        else:    
            messagebox.showinfo ("Informace","Číslo bylo v pořádku.")
    except:
        messagebox.showerror("Chyba","Pozor, hodnota není číslo!")
        w.delete(0,END)

w = Entry(group)
w.pack()
b= Button(group,text="Kontrola",command=kontrola)
b.pack(pady=10)

mainloop()

"""
Napište aplikaci kalkulačka podle zadání na P:
"""    
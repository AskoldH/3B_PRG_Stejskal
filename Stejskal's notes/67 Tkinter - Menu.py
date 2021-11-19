# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:21:14 2013

@author: Radek
"""

from tkinter import *
from tkinter import messagebox
hlavni = Tk()
hlavni.minsize(width=300,height=80)

HorniMenu=Menu(hlavni)
MaleMenu=Menu(hlavni)

def Soubor():
    messagebox.showinfo("Soubor","Tato část není naprogramována!")
    
HorniMenu.add_command(label="Soubor",command=Soubor)
HorniMenu.add_command(label="Nastavení",command=Soubor)
HorniMenu.add_command(label="Nápověda",command=Soubor)
HorniMenu.add_command(label="Konec",command=hlavni.destroy)

MaleMenu.add_command(label="Soubor",command=Soubor)
MaleMenu.add_command(label="Konec",command=hlavni.destroy)

hlavni.config(menu=HorniMenu)

def ZmenMenu():
    hlavni.config(menu=MaleMenu)  

b1=Button(hlavni,text="Menu1",command=lambda:(hlavni.config(menu=HorniMenu)))
b1.pack()
b2=Button(hlavni,text="Menu2",command=ZmenMenu)
b2.pack()



mainloop()
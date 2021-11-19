# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:34:07 2021

@author: stejskal
"""
from tkinter import *

okno = Tk()
okno.title("Náš první program")
okno.minsize(500,300)
okno.maxsize(800,500)
okno.resizable(False,False)

napis = Label(okno,text="Název programu", fg="red",bg="#dddddd", font=("Arial",20))
napis.pack()

tlacitko1 = Button(okno,text="Vypnout",command=okno.destroy)
tlacitko1.pack()

def ZmenNadpis():
    napis["text"]+="!"

tlacitko2 = Button(okno,text="Změň nadpis",command=ZmenNadpis)
tlacitko2.pack()


okno.mainloop()
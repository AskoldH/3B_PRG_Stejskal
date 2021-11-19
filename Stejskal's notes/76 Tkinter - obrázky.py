# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 11:28:18 2015

@author: Radek
"""
"""
Knihovna PIL - umí převádět obrázky na Tkinterovský formát


"""

from Tkinter import *
from PIL import Image, ImageTk 

hlavni = Tk()
 
image = Image.open("pes.jpg") 
photo = ImageTk.PhotoImage(image) 

label = Label(image=photo) 
label.pack() 
tlacitko=Button(image=photo,command=hlavni.destroy)
tlacitko.pack() 


hlavni.mainloop()
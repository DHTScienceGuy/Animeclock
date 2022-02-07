# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:54:53 2022

@author: Art Of DHT
"""

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Anime Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
label = Label(root, font=("Engcomica", 80), background = "White", foreground = "black")
label.pack(anchor='center')
time()

mainloop()
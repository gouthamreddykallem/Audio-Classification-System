# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:11:28 2019

@author: home
"""
from tkinter import *
from winsound import *

class aud:
    def p_a(x):
        root = Tk()
        play = lambda: PlaySound(x, SND_FILENAME)
        button = Button(root, text = 'Play', command = play)
        button.pack(fill=X,pady=20)
        root.mainloop()
        
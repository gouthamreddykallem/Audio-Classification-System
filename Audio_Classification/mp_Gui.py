# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:24:41 2019

@author: home
"""

from tkinter import *
from tkinter import Canvas
from tkinter import Label
import tkinter as tk
import os
from tkinter import filedialog
from PIL import ImageTk
     
#5388d14d.wav

root = tk.Tk()
#root = tk.Toplevel()
C = Canvas(root, height=300, width=300)
w=Label(root, text='Audio classification System', font=("Helvetica", 20))
w2=Label(root, text='Batch C-14', font=("Helvetica", 20))
filename = ImageTk.PhotoImage(file = "griet.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=30, relwidth=1, relheight=1)
w.pack()
w2.pack()
C.pack()

class Audio_file:
    def browse_audio(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Audio File","*.wav",".mp3" )])
        print(self.filename)
        self.n=(os.path.relpath(self.filename, 'D://Audio-Classification-master//wavfiles//'))
    def get_result(self):
        from pre import pred
        x=(pred.prediction(self.n)) 
        global w1
        w1=Label(root, text=x, font=("Helvetica", 16))
        w1.pack()
    def listen(self):
        from play import aud
        aud.p_a(self.filename)


def clear_widget_text(widget):
    widget['text'] = ""

a=Audio_file()

brow_audio = tk.Button(root,width=20,background='blue',foreground='white', text="Audio File", command=a.browse_audio)
brow_audio.pack()

result = tk.Button(root , width=20, background='blue',foreground='white', text="Predict", command=a.get_result)
result.pack()

play = tk.Button(root , width=20, background='blue',foreground='white', text="Play", command=a.listen)
play.pack()

button = tk.Button(root, text="Clear",command=lambda : clear_widget_text(w1))
button.pack()
root.mainloop()


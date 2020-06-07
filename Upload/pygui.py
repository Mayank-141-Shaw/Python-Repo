# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:30:22 2019

@author: MAYANK SHAW
"""

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

ttk.Label(win, text="A Label").grid(column=0, row=0)
ttk.Label(win, text="Second").grid(column=1, row=0)
win.mainloop()

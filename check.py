from tkinter import ttk
import tkinter as tk
from tkinter import *


class VentanaAgregar(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
    
        self.parent=parent            
        width=650
        height=550
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr) 
        
        
        self.check=IntVar()
        self.check.set(0)
        self.btn_check=ttk.Checkbutton(parent,text='Favorita',variable=self.check).grid()
    
root=tk.Tk()
VentanaAgregar(root).mainloop()        

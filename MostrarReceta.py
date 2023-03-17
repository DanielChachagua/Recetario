from tkinter import ttk
from tkinter import *
import tkinter as tk
import os
from os import *
from PIL import Image,ImageTk 
from PIL import *


class MostrarReceta(ttk.Frame):
    def __init__(self,parent,nombre,etiquetas,tiempo_preparacion,tiempo_coccion,ingredientes,imagen,preparacion):
        super().__init__(parent)
        self.parent=parent
        width=1000
        height=600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        parent.geometry(alignstr) 
        
        carpeta_principal=os.path.dirname(__file__)
        self.carpeta_img=os.path.join(carpeta_principal,'media')
        imagen=Image.open(os.path.join(self.carpeta_img,imagen))
        self.img=ImageTk.PhotoImage(imagen)
        imagen_red=imagen.resize((500,400),Image.ANTIALIAS)
        self.img_red=ImageTk.PhotoImage(imagen_red)
        
        self.label_nombre=ttk.Label(parent,text=nombre).grid(row=0,column=1)
        self.label_etiqueta=ttk.Label(parent,text=etiquetas).grid(row=1,column=1)
        self.label_tp=ttk.Label(parent,text=tiempo_preparacion).grid(row=2,column=1)
        self.label_tc=ttk.Label(parent,text=tiempo_coccion).grid(row=2,column=2)
        self.label_ing=ttk.Label(parent,text=ingredientes).grid(row=3,column=1)
        self.label_img=ttk.Label(parent,image=self.img_red).grid(row=0,column=0,rowspan=4)
        self.label_prep=ttk.Label(parent,text=preparacion).grid(row=5,column=0)
     
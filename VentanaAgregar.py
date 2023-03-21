from tkinter import ttk,messagebox
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk 
from Receta import Receta

class VentanaAgregar(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
    
        self.parent=parent
        
        self.nombre=StringVar()
        self.cantidad=IntVar()
        self.unidad=StringVar()
        self.ingrediente=StringVar()
        self.tiempo_prep=IntVar()
        self.tiempo_coc=IntVar()
        self.etiqueta=StringVar()
        self.favorita=IntVar() 
        
        self.tipo=self.fav_boolean()   
                   
        width=650
        height=550
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.parent.geometry(alignstr)
        parent.title('Agregar Recetas') 
        parent.iconbitmap('media/icono_recetario.ico')

        self.frame=ttk.Frame(parent)
        self.frame.grid()
        
        self.btn_imagen=ttk.Button(self.frame,text='Elegir Imagen',command=self.elegir_img)
        self.btn_imagen.grid(row=0,column=0)
        
        self.frame_img=ttk.Frame(self.frame)
        self.frame_img=ttk.LabelFrame(self.frame,text='Imagen')
        self.frame_img.grid(row=1,column=0,rowspan=8)
        self.frame_img.config(width='300',height='230')
       
        self.lb_preparacion=ttk.Label(self.frame,text='Preparación')
        self.lb_preparacion.grid(row=9,column=0)
        self.ent_preparacion=tk.Text(self.frame,width=37,height=12)
        self.ent_preparacion.grid(row=10,column=0,rowspan=8)
        
        self.lb_nombre=ttk.Label(self.frame,text='Nombre Receta',justify='right')
        self.lb_nombre.grid(row=0,column=1)
        self.ent_nombre=ttk.Entry(self.frame,textvariable=self.nombre,justify='center')
        self.ent_nombre.grid(row=0,column=2)
        
        self.frame_ing=ttk.Frame(self.frame)
        self.frame_ing=tk.LabelFrame(self.frame,text='Ingredientes')
        self.frame_ing.grid(row=1,column=1,columnspan=3,rowspan=4)
        
        self.lb_cantidad=ttk.Label(self.frame_ing,text='Cantidad').grid(row=0,column=0)
        self.lb_unidad=ttk.Label(self.frame_ing,text='Unidad').grid(row=0,column=1)
        self.lb_ingrediente=ttk.Label(self.frame_ing,text='Ingrediente').grid(row=0,column=2)
        
        self.ent_cantidad=ttk.Entry(self.frame_ing,textvariable=self.cantidad,width=10,justify='center').grid(row=1,column=0)
        self.ent_unidad=ttk.Entry(self.frame_ing,textvariable=self.unidad,width=10,justify='center').grid(row=1,column=1)
        self.ent_ingrediente=ttk.Entry(self.frame_ing,textvariable=self.ingrediente,width=15,justify='center').grid(row=1,column=2)
        
        def agregar_ing():
            try:
                if self.cantidad.get()!=0 and self.unidad.get()!='' and self.ingrediente.get()!='':
                    cant=self.cantidad.get()
                    un=self.unidad.get()
                    ing=self.ingrediente.get()
                    self.tabla_ing.insert("","end",values=(cant,un,ing))
                    self.cantidad.set(0)
                    self.unidad.set('')
                    self.ingrediente.set('')
                else:
                    messagebox.showinfo(message="Los campos deben de tener algun valor") 
    
            except:    
                messagebox.showinfo(message="Ingrese valores correctos a los campos") 

        self.agregar_ing=ttk.Button(self.frame_ing,text='Agregar',command=lambda:agregar_ing()).grid(row=2,column=0)
        self.eliminar_ing=ttk.Button(self.frame_ing,text='Eliminar',command=lambda:eliminar_ing()).grid(row=2,column=2)

        def eliminar_ing():
            seleccion = self.tabla_ing.selection()
            if seleccion:
                item = self.tabla_ing.item(seleccion) 
                for item in seleccion:
                    self.tabla_ing.delete(item)
            else:
                messagebox.showinfo(message="Debe elegir un elemento primero...")    
            
        columnas = ('Cantidad', 'Unidad', 'Ingrediente')     
        tree_scroll_ing=ttk.Scrollbar(self.frame_ing,orient='vertical')
        tree_scroll_ing.grid(row=3,column=3,sticky=NS)
        self.tabla_ing=ttk.Treeview(self.frame_ing,columns=tuple(columnas),style=None,yscrollcommand=tree_scroll_ing.set,selectmode='browse',show='headings',height=5)
        self.tabla_ing.grid(row=3,column=0,columnspan=3,sticky=EW)
        tree_scroll_ing.config(command=self.tabla_ing.yview)
        
        self.tabla_ing.column('Cantidad',width=70,anchor='center')
        self.tabla_ing.column('Unidad',width=70,anchor='center')
        self.tabla_ing.column('Ingrediente',width=120,anchor='center')
        
        self.tabla_ing.heading('Cantidad',text='Cantidad')
        self.tabla_ing.heading('Unidad',text='Unidad')
        self.tabla_ing.heading('Ingrediente',text='Ingrediente')
        
        self.lb_tiempo_prep=ttk.Label(self.frame,text='Tiempo Preparación')
        self.lb_tiempo_prep.grid(row=8,column=1)
        self.ent_tiempo_prep=ttk.Entry(self.frame,textvariable=self.tiempo_prep,justify='center')
        self.ent_tiempo_prep.grid(row=8,column=2,columnspan=2)
        
        self.lb_tiempo_coc=ttk.Label(self.frame,text='Tiempo Cocción')
        self.lb_tiempo_coc.grid(row=9,column=1)
        self.ent_tiempo_coc=ttk.Entry(self.frame,textvariable=self.tiempo_coc,justify='center')
        self.ent_tiempo_coc.grid(row=9,column=2)
        
        self.lb_etiqueta=ttk.Label(self.frame,text='Etiqueta')
        self.lb_etiqueta.grid(row=10,column=1)
        self.ent_etiqueta=ttk.Entry(self.frame,textvariable=self.etiqueta,justify='center')
        self.ent_etiqueta.grid(row=10,column=2)
        
        self.check_fav=ttk.Checkbutton(self.frame,text='Favorita',variable=self.favorita).grid(row=11,column=1,columnspan=2)
            
        self.btn_guardar=ttk.Button(self.frame,text='Agregar',command=self.guardar)
        self.btn_guardar.grid(row=12,column=1,columnspan=2)
        
        self.btn_salir=ttk.Button(self.frame,text='Salir',command=parent.destroy)
        self.btn_salir.grid(row=13,column=1,columnspan=2)
        
        self.path_img=None
    
    def fav_boolean(self):
            if self.favorita.get()==1:
                return True
            else:
                return False
             
    def obtener_ing(self):
            items=self.tabla_ing.get_children()
            lista_ing=[]
            for item in items:
                it=self.tabla_ing.item(item)
                lista_ing.append(it['values'])
            return lista_ing   
                
    def elegir_img(self):
        self.path_img=filedialog.askopenfilename(filetypes=[
                ('Imagenes',('*.jpg','*.jpeg','*.png')),
                ('Archivos jpg','*.jpg'),
                ('Archivos jpeg','*.jpeg'),
                ('Archivos png','*.png')
            ])
        if self.path_img: 
                self.imagen=Image.open(self.path_img)
                imagen=self.imagen.resize((290,220),Image.LANCZOS)
                self.img=ImageTk.PhotoImage(imagen)
                self.lb_img=ttk.Label(self.frame_img,image=self.img)
                self.lb_img.grid()                 
      
    def guardar(self):
        try:
            if self.path_img!=None:   
                path=self.path_img[::-1]
                ruta_inv=""
                for p in path:
                    if p!='/':
                        ruta_inv+=p
                    else:
                        break
                ruta=ruta_inv[::-1]
                self.imagen.save('media/'+ruta)
            else:
                ruta='sin_imagen.jpg'    
            print(self.fav_boolean())     
            Receta(str(self.nombre.get()),self.obtener_ing(),str(self.ent_preparacion.get('0.0','end')),self.tiempo_prep.get(),self.tiempo_coc.get(),self.ent_etiqueta.get(),ruta,self.fav_boolean).crear_receta()
            messagebox.showinfo(message="Receta guardada con éxito!!!") 
        except:
            messagebox.showerror(message='Asegúrese de cargar bien todos los campos con sus datos correctos')

                
            
# root=tk.Tk()
# VentanaAgregar(root).mainloop()                    

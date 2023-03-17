import datetime
import json

class Receta:
    def __init__(self, nombre, ingredientes, preparacion, tiempo_preparacion, 
                 tiempo_coccion, etiquetas,
                 imagen=None, favorita=False):
        self.nombre=nombre
        self.ingredientes=ingredientes
        self.preparacion=preparacion
        self.imagen=imagen
        self.tiempo_preparacion=tiempo_preparacion
        self.tiempo_coccion=tiempo_coccion
        self.fecha_creacion=(str) (datetime.datetime.now().date())
        self.etiquetas=etiquetas
        self.favorita=favorita
        try:
            with open('recetas.json','x')as archivo:
                data={}
                data['recetas']=[]
                json.dump(data,archivo,indent=4)
        except:
                pass    
        
    def crear_receta(self):
        receta={
            'Nombre':self.nombre,
            'Ingredientes':self.ingredientes,
            'Preparacion':self.preparacion,
            'Imagen':self.imagen,
            'Tiempo_preparacion':self.tiempo_preparacion,
            'Tiempo_coccion':self.tiempo_coccion,
            'Fecha_creacion':self.fecha_creacion,
            'Etiquetas':self.etiquetas,
            'Favorita':self.favorita
        }  
        
        nombre=receta.get('Nombre')          
        with open('recetas.json','r') as archivo:
            lista=json.load(archivo)
        list_receta=[]       
        for list in lista['recetas']:
            list_receta.append(list.get('Nombre'))  
        if nombre not in list_receta:            
            with open ('recetas.json','w') as archivo:
                lista['recetas'].append(receta)
                json.dump(lista,archivo,indent=4)      
                  
    
    def modificar_receta(self):
        try:
            with open('recetas.json','r') as archivo:
                lista=json.load(archivo)    
            indice=None    
            for index,receta in enumerate(lista['recetas']):
                if(receta.get('Nombre') == self.nombre):
                    indice=index   
            receta={
            'Nombre':self.nombre,
            'Ingredientes':self.ingredientes,
            'Preparacion':self.preparacion,
            'Imagen':self.imagen,
            'Tiempo_preparacion':self.tiempo_preparacion,
            'Tiempo_coccion':self.tiempo_coccion,
            'Fecha_creacion':self.fecha_creacion,
            'Etiquetas':self.etiquetas,
            'Favorita':self.favorita
            }      
            with open ('recetas.json','w') as archivo:
                lista['recetas'][indice]=receta        
                json.dump(lista,archivo,indent=4)
        except:
            print('Hubo un problema, no se encuentra elemento!!!')    
    
    def eliminar_receta(nombre):
        try:
            with open('recetas.json','r') as archivo:
                lista=json.load(archivo)  
            for index,receta in enumerate(lista['recetas']):
                if(receta.get('Nombre') == nombre):
                    lista['recetas'].pop(index) 
                    break   
            with open ('recetas.json','w') as archivo:
                json.dump(lista,archivo,indent=4)        
                
        except:
            print('Hubo un problema, no se encuentra elemento!!!')                  
                  
    def receta_del_dia(self):
        pass
    
    def buscar_receta_nombre(nombre):
        try:
            with open('recetas.json','r') as archivo:
                lista=json.load(archivo)
                for receta in lista['recetas']:
                    if receta.get('Nombre')==nombre:
                        return receta
        except:
            pass      
    
    @staticmethod
    def lista_recetas():
        try:
            with open('recetas.json','r') as archivo:
                lista=json.load(archivo)
                return lista['recetas']
        except:
            pass          

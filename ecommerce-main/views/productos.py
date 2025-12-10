from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import MySQLConnection, Error
from datetime import datetime
from tkinter import filedialog, END
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from views.conexion import Conexion
import sys

from CTkListbox import CTkListbox

import sessionmanager


class Productos(CTk):
    



    

    
    def GuardarImagen(self):
        
        filetypes= [("Imagenes","*.png; *.jpg; *.jpeg"), 
            ("todos", "*.*")]
        ruta_guardado=filedialog.askopenfilename(title='Seleccione las imagenes de su producto',
                                                  initialdir=os.getcwd(),
                                                  filetypes=filetypes,
                                                  defaultextension=".jpg")
        if ruta_guardado:
            self.entry_ruta.delete(0,END)
            self.entry_ruta.insert(0,ruta_guardado)
            try:
                self.entry_ruta.delete(0,END)
                self.entry_ruta.insert(0, ruta_guardado)

            except Exception:
                self.entry_ruta.insert(0,ruta_guardado)
                self.imagenes_seleccionadas=ruta_guardado
        
        

    
    def CrearFormulario(self):
        self.Frame_formulario=CTkFrame(self.frameizquierdo, width=500, height=1000, corner_radius=20, fg_color="#EE4D2D")
        self.Frame_formulario.rowconfigure((0), weight=1)
        self.Frame_formulario.columnconfigure((0), weight=1)
        self.Frame_formulario.grid(row=0,column=0, sticky="nsew")

        # Etiquetas y campos de entrada
        self.Label_nombre=CTkLabel(self.Frame_formulario, text="Nombre del producto:", font=('"Segoe UI"',20), fg_color="#EE4D2D", text_color="#FFFFFF")
        self.Label_nombre.place(relx=0.1, rely=0.1)

        self.Entry_nombre=CTkEntry(self.Frame_formulario, width=235, height=30, font=('"Segoe UI"',20))
        self.Entry_nombre.place(relx=0.5, rely=0.1)

        self.Label_categoria=CTkLabel(self.Frame_formulario, text='Categoria', font=('"Segoe UI"',20), fg_color="#EE4D2D",text_color="#FFFFFF")
        self.Label_categoria.place(relx=0.1, rely=0.15)

        self.Entry_categoria = CTkEntry(self.Frame_formulario, width=235, height=30, font=('"Segoe UI"',16))
        self.Entry_categoria.place(relx=0.5, rely=0.15)


        self.listbox_categoria=CTkListbox(self.Frame_formulario, fg_color="#FFFFFF")
        self.listaCategorias= ["Ropa", "Electronica", "Audio y video", "Hogar y Cocina", "Gaming", "Deportes y Aire Libre", "Juguetes y Entretenimiento", "Belleza y Cuidado Personal", "Libros y Papelería", "Accesorios para Vehículos" ]
        for item in self.listaCategorias:
            self.listbox_categoria.insert("end", item)
            
        def _on_select(event):
            sel=self.listbox_categoria.curselection()
            
               
            
            if not sel:
                return
            index = sel[0] if isinstance(sel, (tuple, list)) else sel
            try:
                valor= self.listbox_categoria.get(index)
            except Exception:
                return
            self.categoria_seleccionada=valor
            self.Entry_categoria.delete(0, 'end')
            self.Entry_categoria.insert(0, valor)
            self.listbox_categoria.place_forget()
            self.Entry_categoria.focus_set()
            
        def abrir_categorias():
            self.listbox_categoria.place(relx=0.5, rely=0.18)
            self.listbox_categoria.focus_set()        
                



        self.listbox_categoria.bind("<<ListboxSelect>>", _on_select)
        self.btn_abrir_categorias = CTkButton(self.Frame_formulario, text="Elegir", width=80, height=30, fg_color='#FFFFFF',text_color="#EE4D2D",command=abrir_categorias)
        self.btn_abrir_categorias.place(relx=0.34, rely=0.15)

        self.Label_precio=CTkLabel(self.Frame_formulario, text='Precio:', font=('Segoe UI', 20), fg_color='#EE4D2D', text_color='#FFFFFF')
        self.Label_precio.place(relx=0.1, rely=0.3)

        self.Entry_precio=CTkEntry(self.Frame_formulario, width=235, height=30, font=('"Segoe UI"',20))
        self.Entry_precio.place(relx=0.5, rely=0.3)

        self.Label_descripcion=CTkLabel(self.Frame_formulario, text='Descripción:', font=('"Segoe UI"',20), fg_color="#EE4D2D", text_color="#FFFFFF")
        self.Label_descripcion.place(relx=0.3, rely=0.35)


        

        


        self.Entry_descripcion = CTkTextbox(self.Frame_formulario, width=475, height=250, font=('"Segoe UI"',20))
        self.Entry_descripcion.place(relx=0.02, rely=0.4)
        # asegurar cursor en la primera posición (esquina superior)
        self.Entry_descripcion.delete("1.0", "end")
        self.Entry_descripcion.mark_set("insert", "1.0")
        self.Entry_descripcion.see("1.0")

        self.entry_ruta=CTkEntry(self.Frame_formulario, width=400, height=30,font=('"Segoe UI"',20))
        self.entry_ruta.place(relx=0.1, rely=0.75)


        # boton para abrir imagen
        self.Boton_imagen=CTkButton(self.Frame_formulario, text='Agregar imagen del producto', width=250, height=30, corner_radius=20, fg_color="#FFFFFF",text_color='#EE4D2D',font=('"Segoe UI"',20),command=self.GuardarImagen)
        self.Boton_imagen.place(relx=0.1, rely=0.7)
        self.fecha_producto=datetime.now().date()
        print(self.fecha_producto)
        
        
        

        #Boton para crear producto
        self.boton_crearProducto=CTkButton(self.Frame_formulario, width=150, height=30, text="Crear Producto", corner_radius=20, fg_color="#FFFFFF", text_color='#EE4D2D',font=('"Segoe UI"',20), command=self.CrearProducto )
        self.boton_crearProducto.place(relx=0.3, rely=0.8)
    
            
    
    def CrearProducto(self):
        print("DEBUG: Iniciando CrearProducto")
        self.mi_conexion=Conexion('localhost', 'root', 'root', 'marketplace')

        
        self.conexion = self.mi_conexion.conectar()
        if not self.conexion:
            print("DEBUG: Fallo la conexión.")
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
            return
        

        if self.conexion:
            print('conexion exitosa')
            
            nombre_producto=self.Entry_nombre.get()
            precio_producto=self.Entry_precio.get()
            descripcion_producto=self.Entry_descripcion.get("1.0", "end").strip()
            Ruta_imagen_producto=self.entry_ruta.get()
            categoria = getattr(self, "categoria_seleccionada", "Sin categoría")
            categoria = self.Entry_categoria.get().strip()
            if not categoria:
                categoria = getattr(self, "categoria_seleccionada", "Sin categoría")
            try:
                self.mi_conexion.consulta(("SELECT idCategoria FROM categorias where nombre = %s"), (categoria))
                id_categoria=self.mi_conexion.cursor.fetchone()
                
            

                id_categoria=id_categoria[0]
                print(id_categoria)
                self.mi_conexion.consulta(("INSERT INTO productos (nombre, precio, descripcion, fechaSubido, rutaImagen, idUsuario, idCategoria) VALUES (%s,%s,%s,%s,%s,%s,%s)"),
                                      (nombre_producto, precio_producto,descripcion_producto, str(self.fecha_producto), Ruta_imagen_producto, self.user_id, id_categoria ))
                
                
                
                
                
                #self.mi_conexion.consulta(())
                messagebox.showinfo("Registro exitoso", "Registro completado exitosamente")
                





            except Error as e:
                messagebox.showerror("UPS!", "Algo ha salido mal :(", e)

            
            
                    
            

        
        
        
    

    def __init__(self):
        super().__init__()
        self.ventana_productos=CTk()
        self.ventana_productos.geometry('1000x1000+500+200')
        self.ventana_productos.resizable(False, False)
        self.ventana_productos.configure(corner_radius=20, fg_color="#FFFFFF")
        self.categoria_seleccionada= None
        self.ventana_productos.rowconfigure((0,1), weight=1)
        self.ventana_productos.columnconfigure((0,1), weight=1)
        self.user_id=sessionmanager.id_usuario_actual

        
        
        
        # Frame izquierdo
        self.frameizquierdo=CTkFrame(self.ventana_productos,width=500, height=1000,corner_radius=20, fg_color="#EE4D2D")
        self.frameizquierdo.grid(row=0,column=0, sticky="nsew")

        # Frame derecho
        self.framederecho=CTkFrame(self.ventana_productos,width=500,height=1000)
        self.framederecho.grid(row=0,column=1, sticky="nsew")

        # Botones del menu
        Boton_crearproducto = CTkButton(self.framederecho, text='Agregar Producto', width=150, height=50, fg_color="#EE4D2D", font=("Segoe UI", 20), corner_radius=10, command=self.CrearFormulario)
        Boton_crearproducto.place(relx=0.3, rely=0.3)
        #Metodos
    

        

        self.ventana_productos.mainloop()


        

    


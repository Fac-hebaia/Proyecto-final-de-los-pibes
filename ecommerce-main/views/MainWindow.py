from customtkinter import *
from mysql.connector import *
from views.conexion import Conexion
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PIL import Image, ImageTk
from views.productos import Productos





Imagen_esquina = Image.open("assets/images/imagen.jpg")
Imagen_esquina_editada = Imagen_esquina.resize((200, 200))

# Imagen de la lupa para el buscador
Imagen_lupa = Image.open("assets/images/lupita.jpeg")
Imagen_lupa_editada = Imagen_lupa.resize((39, 39))
# Imagen del logo de whatsapp
Imagen_wp= Image.open("assets/images/whatsapplogo.png")
Imagen_wp= Imagen_wp.resize((30,30))

# Imagen del boton del carrito
imagen_carrito=Image.open("assets/images/carrito.jpeg")
imagen_carrito=imagen_carrito.resize((100,100))

class MainWindow(CTk):

    


            

    def __init__(self):
        super().__init__()

        self.geometry("1500x1500++0+0")
        self.title("Ventana Principal")
        self.configure(fg="#FFFFFF")
        self.resizable(False, False)
        set_appearance_mode("system")

        self.image_references = []
    
        

        
        

        # Frame de la esquina superior con la imagen
        frame = CTkFrame(self, width=200, height=200, corner_radius=20)
        frame.grid(row=0, column=0, padx=10, pady=10)
        labelimagen = ImageTk.PhotoImage(Imagen_esquina_editada)
        Label_imagen = CTkLabel(frame, image=labelimagen, text="")
        Label_imagen.grid(row=0, column=0)

        # Frame Menu izquierdo
        frame_menu = CTkFrame(
            self, width=200, height=1250, corner_radius=20, fg_color="#EE4D2D"
        )
        frame_menu.grid(row=1, column=0, padx=10, pady=10)

        # Botones del menu
        Boton_vender = CTkButton(
            frame_menu,
            text="Vender mis productos",
            width=100,
            height=50,
            fg_color="#EE4D2D",
            font=("Arial", 20),
            corner_radius=10
        )
        Boton_vender.place(relx=0.01, rely=0.05)

    
        
        

        Boton_misproductos = CTkButton(
            frame_menu,
            text="Mis productos",
            width=100,
            height=50,
            fg_color="#EE4D2D",
            font=("Arial", 20),
            corner_radius=10,
            command=self.Abrir_productos
        )
        Boton_misproductos.place(relx=0.01, rely=0.10)

        boton_mispedidos = CTkButton(
            frame_menu,
            text="Mis pedidos",
            width=100,
            height=50,
            fg_color="#EE4D2D",
            font=("Arial", 20),
            corner_radius=10,
        )
        boton_mispedidos.place(relx=0.01, rely=0.15)

        





        
        # Imagen de logo wp
        Icono_wp=ImageTk.PhotoImage(Imagen_wp)
        Label_wp=CTkLabel(frame_menu, image=Icono_wp, width=30, height=30, text="")
        Label_wp.place(relx=0.02, rely=0.2)

        # Label contactenos
        Label_nro=CTkLabel(frame_menu, text="381 350-1563", text_color="#FFFFFF", width=30, font=('"Segoe UI"',20))
        Label_nro.place(relx=0.25, rely=0.2)

        # Frame Menu superior
        frame_superior = CTkFrame(
            self, width=1250, height=200, corner_radius=20, fg_color="#EE4D2D")
        frame_superior.grid(row=0, column=1, padx=10, pady=10)

        # Botones de la parte superior
        carrito=ImageTk.PhotoImage(imagen_carrito)
        boton_carrito=CTkButton(frame_superior, width=100, height=100, text='', image=carrito, fg_color="#EE4D2D", border_width=1, hover_color="#EE4D2D")
        boton_carrito.place(relx=0.5, rely=0.4)

        # Entry de busqueda
        entry_busqueda = CTkEntry(
            frame_superior,
            width=400,
            height=40,
            placeholder_text="Buscar",
            placeholder_text_color="gray",
            font=("Arial", 20),
            corner_radius=10,
        )
        entry_busqueda.place(relx=0.1, rely=0.5)
        # Icono de lupa
        icono_lupa = ImageTk.PhotoImage(Imagen_lupa_editada)
        Label_lupa = CTkLabel(frame_superior, image=icono_lupa, text="")
        Label_lupa.place(relx=0.068, rely=0.5)

        # Frame contenido principal
        self.Frame_contenido = CTkScrollableFrame(self, width=1200, height=1200, corner_radius=20, fg_color="#EE4D2D")
        self.Frame_contenido.grid(row=1, column=1, padx=10, pady=10)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.Catalogo()

    def Catalogo(self):
        self.mi_conexion = Conexion("LocalHost", "root", "root", "marketplace")
        self.mi_conexion.conectar()
    
        if not hasattr(self.mi_conexion, 'cursor') or not self.mi_conexion.cursor:
            print("Conexion fallida")
            return

        try:
            # Limpiar frame
            for widget in self.Frame_contenido.winfo_children():
                widget.destroy()
        
            sql = "SELECT nombre, precio, rutaImagen FROM productos ORDER BY fechaSubido"
            self.mi_conexion.consulta(sql)

            productos = self.mi_conexion.cursor.fetchall()
        
            print(f"Productos encontrados: {len(productos)}")

            self.image_references = []
        
        # Configurar columnas en el ScrollableFrame
            for i in range(4):
                self.Frame_contenido.grid_columnconfigure(i, weight=1)

            if productos:
                row_index = 0
                col_index = 0

                for idx, producto in enumerate(productos):
                    nombre, precio, ruta_imagen = producto
                
                    print(f"Creando producto {idx + 1}: {nombre} en fila {row_index}, col {col_index}")

                    # Frame del producto
                    frame_producto = CTkFrame(
                        self.Frame_contenido,  # Directamente en el scrollable frame
                        width=250,
                    height=350,
                    corner_radius=15,
                    fg_color="#FFFFFF",
                    border_width=2,
                    border_color="#E0E0E0")

                    frame_producto.grid(
                    row=row_index, 
                    column=col_index, 
                    padx=10, 
                    pady=10
                )
                    frame_producto.pack_propagate(False)  # Importante para scrollable frames

                # Cargar imagen
                    try:
                        imagen_pil = Image.open(ruta_imagen)
                        imagen_pil = imagen_pil.resize((230, 230), Image.Resampling.LANCZOS)
                        imagen_ctk = ImageTk.PhotoImage(imagen_pil)

                        self.image_references.append(imagen_ctk)

                        label_imagen = CTkLabel(frame_producto, image=imagen_ctk, text="")
                        label_imagen.pack(pady=(10, 5))

                    except Exception as e:
                        print(f"Error cargando imagen para {nombre}: {e}")
                        label_imagen = CTkLabel(
                        frame_producto, 
                        text="Sin Imagen", 
                        text_color="#999999",
                        font=("Arial", 12)
                    )
                        label_imagen.pack(pady=(10, 5))

                # Nombre del producto
                    CTkLabel(
                    frame_producto,
                    text=nombre,
                    font=("Arial", 16, "bold"),
                    text_color="#333333",
                    wraplength=230
                    ).pack(pady=(5, 2))

                # Precio
                    CTkLabel(
                    frame_producto,
                    text=f"${precio}",
                    font=("Arial", 14, "bold"),
                    text_color="#EE4D2D"
                    ).pack(pady=(2, 10))

                    col_index += 1
                    if col_index == 4:
                        col_index = 0
                        row_index += 1
                    
            else:
                CTkLabel(
                self.Frame_contenido, 
                text="No hay productos en el catálogo.",
                font=("'Segoe UI'", 30)
                    ).grid(row=0, column=0, columnspan=4, pady=20)

        except Exception as e:
            print(f"Error al cargar productos: {e}")
            import traceback
            traceback.print_exc()

        finally:
            self.mi_conexion.cerrar()    

        

    

        self.mainloop()

    def Abrir_productos(self):
        self.destroy()
        productos=Productos()

        


    
   

        

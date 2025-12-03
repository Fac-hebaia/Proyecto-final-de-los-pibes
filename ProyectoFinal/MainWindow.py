from customtkinter import * 
from mysql.connector import *
from conexion import Conexion
from PIL import Image, ImageTk
mi_conexion=Conexion('LocalHost', 'root', 'root', 'proyectomarketplace')
conexion=mi_conexion.conectar()
Imagen_esquina=Image.open('imagen.jpg')
Imagen_esquina_editada=Imagen_esquina.resize((200,200))

#Imagen de la lupa para el buscador
Imagen_lupa=Image.open('lupita.jpeg')
Imagen_lupa_editada=Imagen_lupa.resize((39,39))

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1500x1500++0+0')
        self.title('Ventana Principal')
        self.configure(fg="#FFFFFF")
        self.resizable(False, False)
        set_appearance_mode('system')

        

        # Frame de la esquina superior con la imagen
        frame=CTkFrame(self, width=200, height=200, corner_radius=20)
        frame.grid(row=0, column=0, padx=10, pady=10)
        labelimagen=ImageTk.PhotoImage(Imagen_esquina_editada)
        Label_imagen=CTkLabel(frame, image=labelimagen, text='')
        Label_imagen.grid(row=0, column=0)
        

        # Frame Menu izquierdo
        frame_menu=CTkFrame(self, width=200, height=1250, corner_radius=20, fg_color="#CC2D2D")
        frame_menu.grid(row=1, column=0, padx=10, pady=10)
        
        # Botones del menu
        Boton_vender=CTkButton(frame_menu, text='Vender mis productos', width=100, height=50, fg_color='#CC2D2D', font=('Arial', 20), corner_radius=10)
        Boton_vender.place(relx=0.01, rely=0.05)

        Boton_misproductos=CTkButton(frame_menu, text='Mis productos', width=100, height=50, fg_color='#CC2D2D', font=('Arial', 20), corner_radius=10)
        Boton_misproductos.place(relx=0.01, rely=0.10)

        boton_mispedidos=CTkButton(frame_menu, text='Mis pedidos', width=100, height=50, fg_color='#CC2D2D', font=('Arial', 20), corner_radius=10)
        boton_mispedidos.place(relx=0.01, rely=0.15)

        


        

        # Frame Menu superior
        frame_superior=CTkFrame(self, width=1250, height=200, corner_radius=20, fg_color='#CC2D2D')
        frame_superior.grid(row=0, column=1, padx=10, pady=10)

        # Entry de busqueda
        entry_busqueda=CTkEntry(frame_superior, width=400, height=40, placeholder_text='Buscar', placeholder_text_color='gray', font=('Arial', 20), corner_radius=10)
        entry_busqueda.place(relx=0.1, rely=0.5)
        # Icono de lupa
        icono_lupa=ImageTk.PhotoImage(Imagen_lupa_editada)
        Label_lupa=CTkLabel(frame_superior, image=icono_lupa, text='')
        Label_lupa.place(relx=0.068, rely=0.5)
        
        # Frame contenido principal
        Frame_contenido=CTkFrame(self, width=1250, height=1250, corner_radius=20)
        Frame_contenido.grid(row=1, column=1, padx=10, pady=10)
        


ventana_principal=MainWindow()
ventana_principal.mainloop()



        
    














from conexion import Conexion

from customtkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from mysql.connector import Error
from MainWindow import *

imagen=Image.open("perritosaltando.jpg")
imagen_editada=imagen.resize((500,1000))
mi_conexion=Conexion('LocalHost', 'root', 'root', 'proyectomarketplace')
conexion=mi_conexion.conectar()

class Iniciar_Sesion(CTk):

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        micursor = mi_conexion.connection.cursor()
        micursor.execute('SELECT * FROM usuarios WHERE Email = %s AND Contraseña = %s', (usuario, contraseña))
        resultado = micursor.fetchone()
        try:
            
            if resultado:
                messagebox.showinfo("Inicio de Sesión Exitoso", "Has iniciado sesión correctamente.")
                

                
                
                
                
            else:
                messagebox.showerror("Error de Inicio de Sesión", "Usuario o contraseña incorrectos.")
        except Error as e:
            messagebox.showerror("Hubo un error al iniciar sesión", f'Error: {e}')

    
    def __init__(self):
        super().__init__()
        
        self.title('Iniciar Sesion')
        self.geometry('1000x1000+400+0')
        self.configure(fg_color="#FFFFFF", corner_radius=20)
        self.resizable(False, False)
        set_appearance_mode('system')

        

        


        # Frame de la imagen
        Frame_imagen=CTkFrame(self, width=500, height=1000)
        Frame_imagen.grid(row=0, column=0)
        Label_imagen=ImageTk.PhotoImage(imagen_editada)
        Label_imagen_final=CTkLabel(Frame_imagen, image=Label_imagen, text='')
        Label_imagen_final.grid(row=0, column=0)

        # Frame del Inicio de Sesion
        Frame_inicio=CTkFrame(self, width=500, height=1000, fg_color="#CC2D2D")
        Frame_inicio.grid(row=0, column=1)

        # Labels y Entrys
        self.label_titulo=CTkLabel(Frame_inicio, text='INICIAR SESION', fg_color="#CC2D2D", text_color='white', font=('Times New Roman', 40))
        self.label_titulo.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.label_usuario=CTkLabel(Frame_inicio, text='Usuario', fg_color="#CC2D2D", text_color='white', font=('Arial', 20))
        self.label_usuario.place(relx=0.1, rely=0.35)

        self.label_contraseña=CTkLabel(Frame_inicio, text='Contraseña', fg_color="#CC2D2D", text_color='white', font=('Arial', 20))
        self.label_contraseña.place(relx=0.1, rely=0.45)

        self.entry_usuario=CTkEntry(Frame_inicio, width=300, height=40, font=('Arial', 16))
        self.entry_usuario.place(relx=0.35, rely=0.34)

        self.entry_contraseña=CTkEntry(Frame_inicio, width=300, height=40, font=('Arial', 16), show='*')
        self.entry_contraseña.place(relx=0.35, rely=0.44)

        # Boton Iniciar Sesion
        self.boton_iniciar=CTkButton(Frame_inicio, text='Iniciar Sesion', width=200, height=50, fg_color="#FFFFFF", text_color="#CC2D2D", font=('Arial', 20), command=self.iniciar_sesion)
        self.boton_iniciar.place(relx=0.5, rely=0.6, anchor=CENTER)

        

Inicio_sesion=Iniciar_Sesion()
Inicio_sesion.mainloop()










        





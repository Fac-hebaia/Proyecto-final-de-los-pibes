from tkinter import *
from tkinter import messagebox
from mysql.connector import *
from PIL import Image, ImageTk
from conexion import Conexion

imagen=Image.open("perrito.jpg")
imagen_editada=imagen.resize((500,1000))
mi_conexion=Conexion('LocalHost', 'root', 'root', 'proyectomarketplace')
conexion=mi_conexion.conectar()
class Cliente(Tk):

    def CrearCuenta(self):
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellidos.get()
        contraseña = self.entry_contraseña.get()
        email = self.entry_email.get()
        dni = self.entry_DNI.get()
        pais = self.entry_pais.get()
        provincia = self.entry_provincia.get()
        ciudad = self.entry_ciudad.get()
        codigopostal = self.entry_codigopostal.get()
        direccion = self.entry_direccion.get()
        telefono = self.entry_telefono.get()
        try:
            mi_conexion.consulta('INSERT INTO usuarios (nombres, apellidos, contraseña, email, dni, pais, provincia, ciudad, codigopostal, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            (nombre, apellidos, contraseña, email, dni, pais, provincia, ciudad, codigopostal, direccion, telefono))
            
            
            
            messagebox.showinfo("Registro Exitoso", "Te has registrado exitosamente.")
        except Error as e:
            messagebox.showerror("Hubo un error en el registro", f'Error: {e}')
          
    def __init__(self):
        super().__init__()
        self.geometry('1000x1000+400+0')
        self.configure(bg="#CC2D2D")
        self.resizable(False, False)
        
        self.imagen=ImageTk.PhotoImage(imagen_editada)
        self.frameizq = Frame(self, bg="#CC2D2D", width=500, height=1000)
        self.label_imagen = Label(self.frameizq, image=self.imagen)
        self.label_imagen.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.frameizq.grid(row=0, column=0)
    
      
        
        self.frameder = Frame(self,bg="#CC2D2D", width=400, height=800).grid(row=0, column=1)


        # Labels y Entrys 

        self.registrar = Label(self.frameder, text='REGISTRARSE', bg="#CC2D2D", fg='white', font=('Times New Roman', 20))
        self.registrar.place(relx=0.6, rely=0.2)

        self.label_nombre = Label(self.frameder, text='Nombre', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_nombre.place(relx=0.55, rely=0.3)
        # Entry Nombre
        self.entry_nombre = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_nombre.place(relx=0.7, rely=0.3)


        self.label_apellidos = Label(self.frameder, text='Apellido/s', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_apellidos.place(relx=0.55, rely=0.36)
        # Entry Apellidos
        self.entry_apellidos = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_apellidos.place(relx=0.7, rely=0.36)

        self.label_contraseña = Label(self.frameder, text='Contraseña', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_contraseña.place(relx=0.55, rely=0.42)
        # Entry Contraseña
        self.entry_contraseña = Entry(self.frameder, font=('Arial', 14), width=25, show='*')
        self.entry_contraseña.place(relx=0.7, rely=0.42)

        self.label_email = Label(self.frameder, text='Email', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_email.place(relx=0.55, rely=0.48)
        # Entry Email
        self.entry_email = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_email.place(relx=0.7, rely=0.48)

        self.label_DNI = Label(self.frameder, text='DNI', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_DNI.place(relx=0.55, rely=0.54)
        # Entry DNI
        self.entry_DNI = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_DNI.place(relx=0.7, rely=0.54)

        self.label_pais = Label(self.frameder, text='Pais', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_pais.place(relx=0.55, rely=0.60)
        # Entry Pais
        self.entry_pais = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_pais.place(relx=0.7, rely=0.60)

        self.label_provincia = Label(self.frameder, text='Provincia', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_provincia.place(relx=0.55, rely=0.66)
        # Entry Provincia
        self.entry_provincia = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_provincia.place(relx=0.7, rely=0.66)

         

        self.label_ciudad = Label(self.frameder, text='Ciudad', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_ciudad.place(relx=0.55, rely=0.72)
        # Entry Ciudad
        self.entry_ciudad = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_ciudad.place(relx=0.7, rely=0.72)

        self.label_codigopostal = Label(self.frameder, text='Codigo Postal', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_codigopostal.place(relx=0.55, rely=0.78)
        # Entry Codigo Postal
        self.entry_codigopostal = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_codigopostal.place(relx=0.7, rely=0.78)

        self.label_direccion = Label(self.frameder, text='Direccion', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_direccion.place(relx=0.55, rely=0.84)
        # Entry Direccion
        self.entry_direccion = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_direccion.place(relx=0.7, rely=0.84)

        self.label_telefono = Label(self.frameder, text='Telefono', bg="#CC2D2D", fg='white', font=('Arial', 16))
        self.label_telefono.place(relx=0.55, rely=0.90)
        # Entry Telefono
        self.entry_telefono = Entry(self.frameder, font=('Arial', 14), width=25)
        self.entry_telefono.place(relx=0.7, rely=0.90)

        # Boton Registrar
        self.boton_registrar = Button(self.frameder, text='Registrar', bg='white', fg='#CC2D2D', font=('Arial', 14), command=self.CrearCuenta)
        self.boton_registrar.place(relx=0.65, rely=0.95)

    
        
        
Registro=Cliente()

Registro.mainloop()
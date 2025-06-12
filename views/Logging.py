import tkinter as tk 
from tkinter import *
import time
from views.Tooltip import Tooltip
from views.juego import Juego

class Logging():

    def validar_usuario(self,event):
        self.tool_contraseña.hide_tooltip()
        usuario = self.txtUsuario.get()
        letras=0
        for i in usuario:
            if i.isalpha():
                letras+=1
   
        if usuario.isalnum():
            if len(self.txtUsuario.get()) >= 6 and len(self.txtUsuario.get())<=10:
                if letras >=3:
                    self.tool_usuario.hide_tooltip()
                    self.tool_usuario= Tooltip(self.txtUsuario, "¡Excelente!\nTu nombre de Usuario es valido.",background="#76fa99")
                    self.tool_usuario.show_tooltip()
                    self.estado_usuario="valido"
                else:
                    self.tool_usuario.hide_tooltip()
                    self.tool_usuario= Tooltip(self.txtUsuario, "El usuario debe tener al menos 3 letras.", background="#fa8a76")
                    self.tool_usuario.show_tooltip()
                    self.estado_usuario="invalido"

            elif len(self.txtUsuario.get()) < 6:
                self.tool_usuario.hide_tooltip()
                self.tool_usuario= Tooltip(self.txtUsuario, "El usuario debe tener al menos 6 caracteres.", background="#fa8a76")
                self.tool_usuario.show_tooltip()
                self.estado_usuario="invalido"
            
            elif len(self.txtUsuario.get()) > 10:
                self.tool_usuario.hide_tooltip()
                self.tool_usuario= Tooltip(self.txtUsuario, "El usuario no debe tener más de 15 caracteres.", background="#fa8a76")
                self.tool_usuario.show_tooltip()
                self.estado_usuario="invalido"
        else:
            self.tool_usuario.hide_tooltip()
            self.tool_usuario= Tooltip(self.txtUsuario, "El usuario debe tener SOLO letras y números.\nNO se aceptan caracteres especiales ni espacios",background="#fa8a76")
            self.tool_usuario.show_tooltip()
            self.estado_usuario="invalido"
        
        if self.estado_usuario=="valido":
            self.txtPassword.config(state="normal")
            self.tool_contraseña.hide_tooltip()
            self.tool_contraseña=Tooltip(self.txtPassword, "Ingrese su contraseña. \nminimo 8 carácteres.\nletras y/o números.")
            if event.keysym=="Return":
                self.txtPassword.focus()
        elif self.estado_usuario=="invalido":
            self.txtPassword.config(state="disabled")
            
            

    def validar_contraseña(self,event):
        self.tool_usuario.hide_tooltip()

        if event.keysym == "space" or event.keysym == '.':
            self.tool_contraseña.hide_tooltip()
            self.tool_contraseña= Tooltip(self.txtPassword, "En la contraseña NO se aceptan espacios ni puntos",background="#fa8a76")
            self.tool_contraseña.show_tooltip()
            self.estado_contraseña="invalido"
        else:
            if len(self.txtPassword.get()) >= 6 and len(self.txtPassword.get())<=10:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "¡Excelente!\nTu Contraseña es valida.",background="#76fa99")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="valido"

            elif len(self.txtPassword.get()) < 6:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "El usuario debe tener al menos 6 caracteres.", background="#fa8a76")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="invalido"
            
            elif len(self.txtPassword.get()) > 10:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "La contraseña no debe tener \nmás de 10 caracteres.", background="#fa8a76")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="invalido"


    def verCaracteres(self, event):
        if(self.bandera == True):
            self.txtPassword.config(show='*')
            self.btnVer.config(bg="#ff5810")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(bg="#4fff2c")
            self.bandera = True


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Logging")
        self.ventana.config(width=500, height=450, bg="#12b3b3") 
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg = "#aaff98")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)

        self.lienzo.create_oval(5, 5, 30, 30, fill="#9bb0ec", outline="#0a2e91")
        self.lienzo.create_oval(150, 150, 170, 170, fill="#788fcc", outline="#0a2e91")
        self.lienzo.create_oval(350, 350, 370, 370, fill="#a062c9", outline="#4c0c77")
        self.lienzo.create_oval(380, 60, 400, 80, fill="#8955ac", outline="#4c0c77")
        self.lienzo.create_oval(50, 90, 70, 110, fill="#e0fa6f", outline="#ecdf22")
        self.lienzo.create_oval(400, 250, 420, 270, fill="#e0fa6f", outline="#ecdf22")
        self.lienzo.create_oval(350, 190, 370, 210, fill="#f7829f", outline="#a10e75")
        self.lienzo.create_oval(70, 340, 90, 360, fill="#fa6f92", outline="#a10e75")
        self.lienzo.create_oval(220, 320, 240, 340, fill="#3bbb09", outline="#069e1f")
        self.lienzo.create_oval(280, 70, 300, 90, fill="#3bbb09", outline="#069e1f")

        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help.png")
        self.iconoEntrar = tk.PhotoImage(file=r"Juego\icons\icons8-enter-40.png")
        self.iconoVer = tk.PhotoImage(file=r"Juego\icons\icons8-vision-30.png")
        self.iconoVen = tk.PhotoImage(file=r"Juego\icons\icons8-bmo-80.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Juego\icons\icons8-trash-40.png")
        self.iconoRegis = tk.PhotoImage(file=r"Juego\icons\icons8-add-user-35.png")

        self.lblTitulo = tk.Label(self.ventana, text="Inicio de Sesión", font= ("Arial", 15), bg="#fdebd0")
        self.lblTitulo.place(width=200, height=40, relx=0.5, y=40, anchor="n")

        self.lblIconoVen = tk.Label(self.ventana, image=self.iconoVen, bg="#aaff98")
        self.lblIconoVen.place(width=80, height=80, relx=0.5, y=90, anchor="n")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=400, y=40)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")
                                      
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:", font=("Arial", 12), bg="#fdebd0")
        self.lblUsuario.place(width=120, height=30, x=70, y=200)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(width=150, height=30, x=190, y=200)
        self.tool_usuario= Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nminimo 8 carácteres.\nSolo letras y números.")
        self.txtUsuario.focus()
        self.txtUsuario.bind("<KeyRelease>", self.validar_usuario)
        
        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#fdebd0")
        self.lblPassword.place(width=120, height=30, x=70, y=240)

        self.txtPassword = tk.Entry(self.ventana, show="*", state="disabled")
        self.txtPassword.place(width=150, height=30, x=190, y=240)
        self.tool_contraseña=Tooltip(self.txtPassword, "Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO")
        self.txtPassword.bind("<KeyRelease>", self.validar_contraseña)
   
        self.btnVer = tk.Button(self.ventana, image =self.iconoVer)
        self.btnVer.place(width=30, height=30, x=370, y=240)  
        Tooltip(self.btnVer, "Presione para ver la contraseña")
        self.btnVer.bind("<Button-1>", self.verCaracteres)                    
        
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", image=self.iconoEntrar, compound=LEFT)
        self.btnIngresar.place(width=120, height=40, relx=0.5, y=310)
        Tooltip(self.btnIngresar, "Presione para ingresar el usuario")

        self.btnRegistrarse = tk.Button(self.ventana, text="Registrarse", image=self.iconoRegis, compound=RIGHT)
        self.btnRegistrarse.place(width=120, height=40, relx=0.2, y=310)
        Tooltip(self.btnRegistrarse, "Registrate si no tienes una cuenta")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, x=40, y=370)
        Tooltip(self.btnEliminar, "Presione para eliminar los datos ingresados")

        self.bandera = False
        self.estado_usuario=None
        self.estado_contraseña=None

        self.ventana.mainloop()



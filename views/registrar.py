import tkinter as tk
from tkinter import *
from views.Tooltip import Tooltip
from views.Logging import Logging


class Registro():

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
            self.tool_contraseña.hide_tooltip()
            self.tool_contraseña= Tooltip(self.txtPassword, "Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO",background="#fa8a76")
            self.txtPassword.config(state="disabled")
            
         

    def validar_contraseña(self,event):
        import re
        self.tool_usuario.hide_tooltip()
        contraseña = self.txtPassword.get()
        patron= r"^[a-zA-Z0-9*_-]+$"  # Permite letras, números, *, _ y -
        
        
        if re.match(patron, contraseña):
            if len(contraseña) >= 6 and len(contraseña)<=10:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "¡Excelente!\nTu Contraseña es valida.",background="#76fa99")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="valido"

            elif len(contraseña) < 6:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "La contraseña debe tener al menos 6 caracteres.", background="#fa8a76")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="invalido"
            
            elif len(contraseña) > 10:
                self.tool_contraseña.hide_tooltip()
                self.tool_contraseña= Tooltip(self.txtPassword, "La contraseña no debe tener \nmás de 10 caracteres.", background="#fa8a76")
                self.tool_contraseña.show_tooltip()
                self.estado_contraseña="invalido"

        else:
            self.tool_contraseña.hide_tooltip()
            self.tool_contraseña= Tooltip(self.txtPassword, "En la contraseña SOLO se permiten letras, números, * y _\nNO se aceptan otros caracteres ni espacios",background="#fa8a76")
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
        self.ventana.title("Registro")
        self.ventana.config(width=600, height=550, bg="#12b3b3") 
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg = "#aaff98")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=550, height=500)

        self.iconoUsuario = tk.PhotoImage(file=r"Juego\icons\icons8-user-30.png")
        self.iconoVentana = tk.PhotoImage(file=r"Juego\icons\icons8-sign-in-80.png")
        self.iconoVer = tk.PhotoImage(file=r"Juego\icons\icons8-preview-pane-30.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-eye-50.png")
        self.iconoGuardar = tk.PhotoImage(file=r"Juego\icons\icons8-save-40.png")
        self.iconoEliminar = tk.PhotoImage(file=r"Juego\icons\icons8-trash-40.png")
               
        self.lblTitulo = tk.Label(self.ventana, text="Registrarse", font= ("Arial", 15), bg="#def1f7")
        self.lblTitulo.place(width=200, height=40, relx=0.5, y=50, anchor="n")

        self.lblIconoVentana = tk.Label(self.ventana, image=self.iconoVentana, bg="#aaff98")
        self.lblIconoVentana.place(width=80, height=80, relx=0.5, y=120, anchor="n")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda, bg="#def1f7")
        self.btnAyuda.place(width=50, height=50, x=495, y=50)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:", image=self.iconoUsuario, compound=LEFT, font=("Arial", 12), bg="#def1f7")
        self.lblUsuario.place(width=120, height=30, x=70, y=240)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(width=150, height=30, x=190, y=240)
        self.tool_usuario= Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nminimo 8 carácteres.\nSolo letras y números.")
        self.txtUsuario.focus()
        self.txtUsuario.bind("<KeyRelease>", self.validar_usuario)

        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#def1f7")
        self.lblPassword.place(width=120, height=30, x=70, y=290)

        self.txtPassword = tk.Entry(self.ventana, show="*",state="disabled")
        self.txtPassword.place(width=150, height=30, x=190, y=290)
        self.tool_contraseña=Tooltip(self.txtPassword, "Para poder crear una contraseña primero \ncree un nombre de usuario VALIDO")
        self.txtPassword.bind("<KeyRelease>", self.validar_contraseña)
   
        self.btnVer = tk.Button(self.ventana, image =self.iconoVer, bg="#ff5810")
        self.btnVer.place(width=30, height=30, x=370, y=290) 
        Tooltip(self.btnVer, "Presione para ver la contraseña")
        self.btnVer.bind("<Button-1>", self.verCaracteres) 

        self.lblPassword2= tk.Label(self.ventana, text=" Confirmar Contraseña*:", font=("Arial", 8), bg="#def1f7")
        self.lblPassword2.place(width=120, height=30, x=70, y=340)

        self.txtPassword2 = tk.Entry(self.ventana, show="*",state="disabled")
        self.txtPassword2.place(width=150, height=30, x=190, y=340)
        Tooltip(self.txtPassword2, "Ingrese su contraseña nuevamente. \nSolo números.")

        self.btnVer2 = tk.Button(self.ventana, image =self.iconoVer, bg="#ff5810")
        self.btnVer2.place(width=30, height=30, x=370, y=340)
        Tooltip(self.btnVer2, "Presione para ver la contraseña")
        self.btnVer2.bind("<Button-1>", self.verCaracteres) 

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", font=("Arial", 12), image=self.iconoGuardar, compound=LEFT)
        self.btnGuardar.place(width=120, height=40, relx=0.5, y=410)
        Tooltip(self.btnGuardar, "Presione para guardar \nla información de usuario")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, x=200, y=410)
        Tooltip(self.btnEliminar, "Presione para eliminar \nlos datos ingresados")

        self.bandera = False
        self.estado_usuario=None
        self.estado_contraseña=None
   
        self.ventana.mainloop()
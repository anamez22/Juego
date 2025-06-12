import tkinter as tk
from tkinter import *
from views.Tooltip import Tooltip
from views.Logging import Logging


class Registro():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro")
        self.ventana.config(width=600, height=550, bg="#12b3b3") 
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg = "#aaff98")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=550, height=500)

        self.iconoUsuario = tk.PhotoImage(file=r"icons\icons8-user-30.png")
        self.iconoVentana = tk.PhotoImage(file=r"icons\icons8-sign-in-80.png")
        self.iconoVer = tk.PhotoImage(file=r"icons\icons8-preview-pane-30.png")
        self.iconoAyuda = tk.PhotoImage(file=r"icons\icons8-help-eye-50.png")
        self.iconoGuardar = tk.PhotoImage(file=r"icons\icons8-save-40.png")
        self.iconoEliminar = tk.PhotoImage(file=r"icons\icons8-trash-40.png")
               
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
        Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nSolo letras minúsculas.")

        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#def1f7")
        self.lblPassword.place(width=120, height=30, x=70, y=290)

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(width=150, height=30, x=190, y=290)
        Tooltip(self.txtPassword, "Ingrese su contraseña. \nSolo números.")

        self.btnVer = tk.Button(self.ventana, image =self.iconoVer)
        self.btnVer.place(width=30, height=30, x=370, y=290) 
        Tooltip(self.btnVer, "Presione para ver la contraseña")

        self.lblPassword2= tk.Label(self.ventana, text=" Confirmar Contraseña*:", font=("Arial", 8), bg="#def1f7")
        self.lblPassword2.place(width=120, height=30, x=70, y=340)

        self.txtPassword2 = tk.Entry(self.ventana, show="*")
        self.txtPassword2.place(width=150, height=30, x=190, y=340)
        Tooltip(self.txtPassword2, "Ingrese su contraseña nuevamente. \nSolo números.")

        self.btnVer2 = tk.Button(self.ventana, image =self.iconoVer)
        self.btnVer2.place(width=30, height=30, x=370, y=340)
        Tooltip(self.btnVer2, "Presione para ver la contraseña")

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", font=("Arial", 12), image=self.iconoGuardar, compound=LEFT)
        self.btnGuardar.place(width=120, height=40, relx=0.5, y=410)
        Tooltip(self.btnGuardar, "Presione para guardar \nla información de usuario")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, x=200, y=410)
        Tooltip(self.btnEliminar, "Presione para eliminar \nlos datos ingresados")
   
        self.ventana.mainloop()
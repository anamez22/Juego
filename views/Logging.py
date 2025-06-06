import tkinter as tk 
from tkinter import *
from views.Tooltip import Tooltip
from views.juego import Juego

class Logging():
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

        self.iconoAyuda = tk.PhotoImage(file=r"icons\icons8-help.png")
        self.iconoEntrar = tk.PhotoImage(file=r"icons\icons8-enter-40.png")
        self.iconoVer = tk.PhotoImage(file=r"icons\icons8-vision-30.png")
        self.iconoVen = tk.PhotoImage(file=r"icons\icons8-bmo-80.png")
        self.iconoEliminar = tk.PhotoImage(file=r"icons\icons8-trash-40.png")

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
        Tooltip(self.txtUsuario, "Ingrese su nombre de usuario.\nSolo letras minúsculas.")
        
        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:", font=("Arial", 12), bg="#fdebd0")
        self.lblPassword.place(width=120, height=30, x=70, y=240)

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(width=150, height=30, x=190, y=240)
        Tooltip(self.txtPassword, "Ingrese su contraseña. \nSolo números.")
   
        self.btnVer = tk.Button(self.ventana, image =self.iconoVer)
        self.btnVer.place(width=30, height=30, x=370, y=240)  
        Tooltip(self.btnVer, "Presione para ver la contraseña")                      
        
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", image=self.iconoEntrar, compound=LEFT)
        self.btnIngresar.place(width=120, height=40, relx=0.5, y=310)
        Tooltip(self.btnIngresar, "Presione para ingresar el usuario")

        self.btnEliminar = tk.Button(self.ventana, image=self.iconoEliminar)
        self.btnEliminar.place(width=40, height=40, relx=0.3, y=310)
        Tooltip(self.btnEliminar, "Presione para eliminar los datos ingresados")

        self.ventana.mainloop()

   
import tkinter as tk 
from tkinter import * 
from views.Tooltip import Tooltip
from PIL import Image, ImageTk

from Controllers.Tuberias import Tuberias

class Juego():

    def comenzarJuego(self,event):
        self.tuberia = Tuberias(self.lienzo)
        self.tuberia.iniciar_movimiento()
        #aca puede crear el objeto de la clase pajaro q va a crear para que ejecute las funciones suyas
        #porque pues esta funcion es la que se ejecuta al presionar el boton jugar

        #aqui vamos a ejcutar las funciones de las clases que se creen en otros archivos 
        


    def paint(self):
        cuerpo = self.lienzo.create_oval(10, 270, 75, 330, fill="#fcf83b", tags="cuerpo")
        ala = self.lienzo.create_oval(7, 295, 37, 315, fill="#ffffff", tags="ala")
        ojo = self.lienzo.create_oval(55, 275, 80, 300, fill="#ffffff", tags="ojo")
        pupila = self.lienzo.create_oval(67, 285, 77, 295, fill="#000102", tags="pupila")
        boca = self.lienzo.create_oval(65, 302, 85, 310, fill="#F38C47")

        alaArriba = self.lienzo.create_oval(7, 285, 37, 305, fill="#ffffff", tags="ala_arriba")
        alaabajo = self.lienzo.create_oval(7, 305, 37, 325, fill="#ffffff", tags="ala_abajo")

        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("JUEGO HAPPY BIRD")
        self.ventana.config(width=900, height=700, bg="#000000")
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg="#94caca")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=800, height=640)

        self.iconoJugar = tk.PhotoImage(file=r"Juego\icons\icono_play.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-50.png")
        
        self.btnJugar = tk.Button(self.ventana, image=self.iconoJugar, bg="#dde38d")
        self.btnJugar.place(relx=0.5, rely=1, y=-53, anchor="center", width=105, height=44)
        Tooltip(self.btnJugar, "Presione para iniciar el juego")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=780, y=50)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")
 
        self.lblPuntaje = tk.Label(self.lienzo, text="Puntaje", font= ("Arial", 14))
        self.lblPuntaje.place(relx=0.5, y=30, anchor="center")

        self.lienzo.create_rectangle(0, 590, 800, 640, fill="#dde38d", outline="#33b812", width=5)
        
        self.paint()
        self.btnJugar.bind("<Button-1>", self.comenzarJuego)


        self.ventana.mainloop()
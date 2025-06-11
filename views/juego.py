import tkinter as tk 
from tkinter import * 
from views.Tooltip import Tooltip
from PIL import Image, ImageTk

from Controllers.Tuberias import Tuberias
from Controllers.isabella import Manejo_Pajaro

class Juego():

    def comenzarJuego(self,event):
        self.tuberia = Tuberias(self.lienzo)
        self.pajaro = Manejo_Pajaro(self.lienzo)
        self.actualizarJuego()
    
    def moverPajaro(self,event):
        if hasattr(self, 'pajaro'): #Verifica si el pajaro ha sido creado
            self.pajaro.saltar(event)
    
    def actualizarJuego(self):
         if hasattr(self, 'pajaro'):
             self.pajaro.actualizar_posicion()
             self.lienzo.after(30, self.actualizarJuego) #llama la funcion cada 30 milisegundos
    

        


    def paint(self):
       
        self.lienzo.create_oval(200, 270, 265, 330, fill="#fcf83b", tags="cuerpo")           # cuerpo
        self.lienzo.create_oval(197, 295, 227, 315, fill="#ffffff", tags="ala")              # ala
        self.lienzo.create_oval(245, 275, 270, 300, fill="#ffffff", tags="ojo")              # ojo
        self.lienzo.create_oval(257, 285, 267, 295, fill="#000102", tags="pupila")           # pupila
        self.lienzo.create_oval(255, 302, 275, 310, fill="#F38C47", tags="boca")             # boca

        self.lienzo.create_oval(197, 285, 227, 305, fill="#ffffff", tags="ala_arriba")       # ala arriba
        self.lienzo.create_oval(197, 305, 227, 325, fill="#ffffff", tags="ala_abajo")  

        
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("JUEGO HAPPY BIRD")
        self.ventana.config(width=900, height=700, bg="#000000")
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg="#94caca")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=800, height=640)
        self.lienzo.focus_set() # Esto permite que el lienzo reciba eventos de teclado

        self.iconoJugar = tk.PhotoImage(file=r"Juego\icons\icono_play.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-50.png")
        self.iconoNube = tk.PhotoImage(file=r"Juego\icons\icons8-clouds-100.png")
        
        self.btnJugar = tk.Button(self.ventana, image=self.iconoJugar, bg="#dde38d")
        self.btnJugar.place(relx=0.5, rely=1, y=-53, anchor="center", width=105, height=44)
        Tooltip(self.btnJugar, "Presione para iniciar el juego")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=780, y=50)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")

        self.lblIconoNube = tk.Label(self.lienzo, image=self.iconoNube, bg="#94caca")
        self.lblIconoNube.place(width=100, height=100, relx=0.5, y=90, anchor="n")
        
        self.lblPuntaje = tk.Label(self.lienzo, text="Puntaje", font= ("Arial", 14))
        self.lblPuntaje.place(relx=0.5, y=30, anchor="center")

        self.lienzo.create_rectangle(0, 590, 800, 660, fill="#dde38d", outline="#33b812", width=5)
        
        self.paint()
        self.btnJugar.bind("<Button-1>", self.comenzarJuego)
        self.lienzo.bind("<space>", self.moverPajaro)
        


        self.ventana.mainloop()
import tkinter as tk 
from tkinter import * 
from views.Tooltip import Tooltip
from PIL import Image, ImageTk

class Juego():
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
        self.ventana.config(width=900, height=700, bg="#000102")
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg="#94caca")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=800, height=600)

        imagenTronco = Image.open(r"icons\woods.png")
        imagentk = ImageTk.PhotoImage(imagenTronco)
        image = self.lienzo.create_image(300, 445, image=imagentk) 

        self.iconoJugar = tk.PhotoImage(file=r"icons\icons8-play-40.png")
        self.iconoAyuda = tk.PhotoImage(file=r"icons\icons8-help-50.png")
        self.iconoNube = tk.PhotoImage(file=r"icons\icons8-clouds-100.png")
        
        self.btnJugar = tk.Button(self.ventana, image=self.iconoJugar)
        self.btnJugar.place(relx=0.5, rely=1, y=-27, anchor="center", width=40, height=40)
        Tooltip(self.btnJugar, "Presione para iniciar el juego")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=780, y=70)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")

        self.lblIconoNube = tk.Label(self.ventana, image=self.iconoNube, bg="#94caca")
        self.lblIconoNube.place(width=100, height=100, relx=0.5, y=90, anchor="n")
        
        self.lblPuntaje = tk.Label(self.lienzo, text="Puntaje", font= ("Arial", 14))
        self.lblPuntaje.place(relx=0.5, y=30, anchor="center")

        self.lienzo.create_rectangle(0, 570, 800, 600, fill="#f6ff7a", outline="#4fe729", width=5)

        
        self.paint()
        self.ventana.mainloop()
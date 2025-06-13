import tkinter as tk 
from tkinter import * 
from views.Tooltip import Tooltip
from PIL import Image, ImageTk
import threading as th
import time
from tkinter import messagebox as mb


from Controllers.Tuberias import Tuberias
from Controllers.pajaro import Manejo_Pajaro

class Juego():

    instacia_juego=None

    def limpiar_juego(self,event):
        tuberias_hechas=self.tuberia.tuberias_funcionando

        for tuberia in tuberias_hechas:
            self.lienzo.delete("tuberia")
        
        if hasattr(self, 'pajaro'): #Verifica si el pajaro ha sido creado
            self.lienzo.delete("pajaro")
        self.paint()
      

    def reiniciar_juego(self):
        pass

    def comenzarJuego(self,event):
        if event.keysym =="c":

            if self.juego_activo:#no deja que se cree otro hilo hasta que el anterior termine su ciclo
                    return
                        
            self.juego_activo=True
            #self.btnJugar.config(state="disabled")
            self.tuberia=Tuberias(self.lienzo,self) #self llama al self.juego de las tuberias
            self.tuberia.iniciar_movimiento()#crear el hilo que mueve el objeto 
        
            self.pajaro = Manejo_Pajaro(self.lienzo)       
            self.actualizarJuego()
            self.lienzo.focus_set() 
            
        
    def moverPajaro(self,event):
        if hasattr(self, 'pajaro'): #Verifica si el pajaro ha sido creado
            self.pajaro.saltar(event)
    
    def actualizarJuego(self):
     if self.juego_activo and hasattr(self, 'pajaro'):
        self.pajaro.actualizar_posicion()
        self.lienzo.after(30, self.actualizarJuego)
       

    def  hilo_colisiones(self):
        hilo_colision=th.Thread(target=self.detectar_colisiones)
        hilo_colision.daemon=True #Evita que cuando el jugador pierda el hilo se quede en segundo plano
        hilo_colision.start()
    
    def detectar_colisiones(self):
        while True:
            if hasattr(self,"pajaro"): #ya existe pajaro?
                pajaro_coordenadas = self.lienzo.bbox("pajaro") #bbox: cuadro delemitador que devuelve una tupla de 4 numeros que son las coordenadas de los rectangulos
                for tuberia in Tuberias.tuberias_funcionando:
                    t1=self.lienzo.bbox(tuberia.tuberia1)
                    t2=self.lienzo.bbox(tuberia.tuberia2)

                    if self.colision(pajaro_coordenadas,t1) or self.colision(pajaro_coordenadas,t2):
                        self.game_over()
                        return
                time.sleep(0.01)
    def colision(self,r1, r2):  # r=rectangulos
        r1_izq, r1_arriba, r1_dere, r1_abajo = r1
        r2_izq, r2_arriba, r2_der, r2_abajo = r2
        no_colision = (
            r1_dere < r2_izq or   
            r1_izq > r2_der or    
            r1_abajo < r2_arriba or  
            r1_arriba > r2_abajo     
        )
        return not no_colision
    
    
    def game_over(self):
        self.juego_activo = False  # Detiene el bucle del juego
        self.btnJugar.config(state="normal")
        self.lienzo.create_text(400, 320, text="GAME OVER", fill="black", font=("Arial", 40))

        if hasattr(self, "pajaro"):
            self.pajaro.detener()  # Detiene al pájaro 
    
    def aumentar_puntaje(self):
        self.puntaje +=1
        self.lblPuntaje.config(text=f"Puntaje:{self.puntaje}")



    def paint(self):
       
        self.lienzo.create_oval(200, 270, 265, 330, fill=self.color_pajaro, tags="pajaro")           
        self.lienzo.create_oval(245, 275, 270, 300, fill="#ffffff", tags="pajaro")              
        self.lienzo.create_oval(257, 285, 267, 295, fill="#000102", tags="pajaro")           
        self.lienzo.create_oval(255, 302, 275, 310, fill="#F38C47", tags="pajaro")             

        self.lienzo.create_oval(194, 290, 228, 313, fill="#ffffff", tags="pajaro")       

        
    def __init__(self):
        self.puntaje=0
        self.juego_activo=False
        self.color_pajaro="#fcf83b"
        self.ventana = tk.Tk()
        self.ventana.title("JUEGO HAPPY BIRD")
        self.ventana.config(width=900, height=700, bg="#000000")
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg="#94caca")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=800, height=640)
        self.lienzo.focus_set() # Esto permite que el lienzo reciba eventos de teclado

        self.imagenFondo = tk.PhotoImage(file=r"Juego\icons\fondo juego.png")
        self.lienzo.create_image(0, 0, image=self.imagenFondo, anchor="nw", tags="fondo")

        self.iconoJugar = tk.PhotoImage(file=r"Juego\icons\icono_play.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-50.png")
        self.verPuntajes = tk.PhotoImage(file=r"Juego\icons\icons8-mac-folder-50.png")
        
        
        self.btnJugar = tk.Button(self.ventana, image=self.iconoJugar, bg="#dde38d",state="disabled")
        self.btnJugar.place(relx=0.5, rely=1, y=-53, anchor="center", width=105, height=44)
        Tooltip(self.btnJugar, "Presione para iniciar el juego")

        self.btnAyuda = tk.Button(self.ventana, image=self.iconoAyuda)
        self.btnAyuda.place(width=50, height=50, x=780, y=50)
        Tooltip(self.btnAyuda, "Presione para ver la ayuda")
 
        self.lblPuntaje = tk.Label(self.lienzo, text="Puntaje: 0",  font=("Comic Sans MS", 18, "bold"),bg="#94caca", fg="#175e0d",relief="raised", bd=4)
        self.lblPuntaje.place(relx=0.5, y=30, anchor="center")

        self.btnPuntajes = tk.Button(self.ventana, image=self.verPuntajes)
        self.btnPuntajes.place(width=50 ,height=50, x=70, y=50)
        Tooltip(self.btnPuntajes, "Presione para ver los \n puntajes de los jugadores")

        self.lienzo.create_rectangle(0, 590, 800, 640, fill="#dde38d", outline="#33b812", width=5)
        
        self.paint()
        
        self.btnJugar.bind("<Button-1>", self.limpiar_juego)
        self.ventana.bind("<KeyRelease>", self.comenzarJuego)
        self.lienzo.bind("<space>", self.moverPajaro)
        self.hilo_colisiones()
        self.pajaro="pajaro"

        self.ventana.mainloop()
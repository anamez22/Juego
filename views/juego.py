import tkinter as tk 
from tkinter import * 
from views.Tooltip import Tooltip
from PIL import Image, ImageTk
import threading as th
import time
from tkinter import messagebox as mb

from Controllers.sonidos import manejar_sonidos
from Controllers.Tuberias import Tuberias
from Controllers.pajaro import Manejo_Pajaro

class Juego():

    instacia_juego=None

    def reiniciar_juego(self,event):
        self.boton_reiniciar.place_forget()
        self.lienzo_game_over.destroy()  
        self.btnJugar.place(relx=0.5, rely=1, y=-53, anchor="center", width=105, height=44)
        self.lienzo.create_text(400, 550, text="Para saltar Presione la tecla de espacio", font=("Arial", 16), fill="black", tags="texto")

        self.puntaje=0
        self.lblPuntaje.config(text=f"Puntaje:{self.puntaje}")

        tuberias_hechas=self.tuberia.tuberias_funcionando

        for tuberia in tuberias_hechas:
            self.lienzo.delete("tuberia")
        
        if hasattr(self, 'pajaro'): #Verifica si el pajaro ha sido creado
            self.lienzo.delete("pajaro")

        self.juego_activo = False  # reiniciar estado del juego
        self.paint()
        self.btnJugar.config(state="normal")# vuelve a crear el lienzo
        self.bandera=True
    
        

    def comenzarJuego(self,event):
        if self.juego_activo:#no deja que se cree otro hilo hasta que el anterior termine su ciclo
                    return
        self.lienzo.delete("texto")               
        self.juego_activo=True
        self.btnJugar.config(state="disabled")
        self.hilo_colisiones() 
        self.tuberia=Tuberias(self.lienzo,self) #self llama al self.juego de las tuberias
        self.pajaro=Manejo_Pajaro(self.lienzo) 
        
        self.tuberia.iniciar_movimiento()#crear el hilo que mueve el objeto 
        
        self.actualizarJuego()
        self.lienzo.focus_set() 
            
        
    def moverPajaro(self,event):
        if hasattr(self, 'pajaro'): #Verifica si el pajaro ha sido creado
            self.pajaro.saltar(event)
            if self.bandera:
                manejar_sonidos(vuelo=True)
    
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
                if pajaro_coordenadas is None:
                    time.sleep(0.01)
                    continue
                
                for tuberia in Tuberias.tuberias_funcionando:
                    t1=self.lienzo.bbox(tuberia.tuberia1)
                    t2=self.lienzo.bbox(tuberia.tuberia2)

                    # Verifica que t1 y t2 no sean None
                    if t1 and self.colision(pajaro_coordenadas, t1):
                        manejar_sonidos(gameover=True)
                        self.game_over()
                        return
                    if t2 and self.colision(pajaro_coordenadas, t2):
                        manejar_sonidos(gameover=True)
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
    

    def game_over(self):#BASE DE DATOS
        #por aqui se puede ir guardando el puntaje que obtenga el usuario, 
        # y con la base de datos comparar el puntaje anterior guardado con el que obtiene al volver a jugar para que en la lista se muestren los puntajes maximos  de los jugadores
        self.juego_activo = False  # Detiene el bucle del juego
        self.bandera=False
        if hasattr(self, "pajaro"):
            self.pajaro.detener()  # Detiene al pájaro
        self.lienzo.itemconfig("cuerpo",fill="#fc753b")
        if self.puntaje>self.best_score:
            self.best_score=self.puntaje
        
        self.mostrar_ventana2()
        
    
    def aumentar_puntaje(self):
        self.puntaje +=1
        self.lblPuntaje.config(text=f"Puntaje:{self.puntaje}")


    def paint(self):

        self.lienzo.create_oval(200, 270, 265, 330, fill="#fcf83b", tags=("pajaro","cuerpo"))           
        self.lienzo.create_oval(245, 275, 270, 300, fill="#ffffff", tags="pajaro")              
        self.lienzo.create_oval(257, 285, 267, 295, fill="#000102", tags="pajaro")           
        self.lienzo.create_oval(255, 302, 275, 310, fill="#F38C47", tags="pajaro")             

        self.lienzo.create_oval(194, 290, 228, 313, fill="#ffffff", tags="pajaro")  

    def mostrar_ventana2(self):
        self.btnJugar.place_forget()
        from tkinter import font
        self.lienzo_game_over=tk.Canvas(self.lienzo,bg="#e8be13")
        fuente= font.Font(family="Comic Sans MS", size=24, weight="bold")
        self.lienzo_game_over.place(relx=0.5,rely=0.5,anchor="center", width=400,height=400)
        self.lienzo_game_over.create_image(200,90,image=self.gameover)
        self.lienzo_game_over.create_rectangle(50,175,350,310,fill="#fffd82", outline="#fffd82")
        label_score=tk.Label(self.lienzo_game_over, text=f"SCORE: {self.puntaje}", font=fuente,fg="black", bg="#fffd82")
        label_score.place(x=60,y=185)
        label_best_score=tk.Label(self.lienzo_game_over, text=f"BEST: {self.best_score}", font=fuente,fg="black", bg="#fffd82")
        label_best_score.place(x=60, y=250)

        self.boton_reiniciar.place(relx=0.5, y=505, anchor="center",width=100, height=60)
        


        
    def __init__(self):
        self.puntaje=0
        self.best_score=0
        self.juego_activo=False
        self.ventana = tk.Tk()
        self.ventana.title("JUEGO FLAPPY BIRD")
        self.ventana.config(width=900,height=700,bg="#000000")
        self.ventana.resizable(0,0)

        self.lienzo = tk.Canvas(self.ventana, bg="#94caca")
        self.lienzo.place(relx=0.5, rely=0.5, anchor="center", width=800, height=640)
        self.lienzo.focus_set() # Esto permite que el lienzo reciba eventos de teclado

        self.imagenFondo = tk.PhotoImage(file=r"Juego\icons\fondo juego.png")
        self.lienzo.create_image(0, 0, image=self.imagenFondo, anchor="nw", tags="fondo")

        self.iconoJugar = tk.PhotoImage(file=r"Juego\icons\icono_play.png")
        self.iconoAyuda = tk.PhotoImage(file=r"Juego\icons\icons8-help-50.png")
        self.verPuntajes = tk.PhotoImage(file=r"Juego\icons\icons8-mac-folder-50.png")
        self.gameover=tk.PhotoImage(file=r"Juego\icons\gameover.png")
        self.iconoplay=tk.PhotoImage(file=r"Juego\icons\iconoplaygame.png")
        
        
        self.btnJugar = tk.Button(self.ventana, image=self.iconoJugar, bg="#dde38d",state="normal")
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

        self.boton_reiniciar=tk.Button(self.ventana, image=self.iconoplay,bg="white",compound="center")
        Tooltip(self.boton_reiniciar, "Presione para volver a jugar")

        self.lienzo.create_text(400, 550, text="Para saltar Presione la tecla de espacio", font=("Arial", 16), fill="black", tags="texto")
        self.lienzo.create_rectangle(0, 590, 800, 640, fill="#dde38d", outline="#33b812", width=5)
        
        self.paint()        
        self.hilo_colisiones()
        self.lienzo.bind("<space>", self.moverPajaro)
        self.boton_reiniciar.bind("<Button-1>", self.reiniciar_juego)
        self.btnJugar.bind("<Button-1>", self.comenzarJuego)

        self.bandera=True
    
        self.ventana.mainloop()
import random
import threading as th
import time

class Tuberias:
    tuberias_funcionando=[]

    def iniciar_movimiento(self, *args):
        hilo1 = th.Thread(target=self.actualizar_tuberias)
        hilo1.start()   


    def dibujar(self):
        self.tuberia1=self.lienzo.create_rectangle(680+self.x, 0, 790+self.x, self.obstaculo, fill=self.color, tags="tuberia")
        self.tuberia2=self.lienzo.create_rectangle(680+self.x, self.obstaculo+175, 790+self.x, 590, fill=self.color, tags="tuberia" )
       

        self.decoracion1=self.lienzo.create_rectangle(670+self.x, self.obstaculo-50, 800+self.x, self.obstaculo, fill=self.color, tags="tuberia")
        self.decoracion2=self.lienzo.create_rectangle(670+self.x, self.obstaculo+175, 800+self.x, self.obstaculo+225, fill=self.color, tags="tuberia")
  
   
    def mover_tuberias(self):
        self.x -= self.velocidad
        self.lienzo.move(self.tuberia1, -self.velocidad, 0)
        self.lienzo.move(self.tuberia2, -self.velocidad, 0)
        self.lienzo.move(self.decoracion1, -self.velocidad, 0)
        self.lienzo.move(self.decoracion2, -self.velocidad, 0)
        if not self.contar:
         coords = self.lienzo.bbox(self.tuberia1)
         if coords is not None and coords[2] < 200:
          self.contar = True
          try:
            self.juego.aumentar_puntaje()  
          except Exception as e:
            print("Error al aumentar puntaje:", e)
      

    def actualizar_tuberias(self):
        while self.juego.juego_activo:#cuando self.juego_activo sea False el hilo creado termina su ciclo
            for tuberia in Tuberias.tuberias_funcionando:
                tuberia.mover_tuberias()
                if tuberia.x < -800:
                    Tuberias.tuberias_funcionando.remove(tuberia)
            if (not Tuberias.tuberias_funcionando) or (Tuberias.tuberias_funcionando[-1].x <= -300):
                Tuberias(tuberia.lienzo, tuberia.juego)
            time.sleep(0.016)
    
       
                
    def __init__(self, lienzo,juego):
        self.juego=juego
        self.contar=False
        self.lienzo = lienzo
        self.x = 0
        self.y = 0
        self.obstaculo=random.randint(70,330) 
        self.velocidad = 2.5
        self.color = "#33b812"

        self.dibujar()
        Tuberias.tuberias_funcionando.append(self)#guarda la referencia del objeto que se crea
       



        

        
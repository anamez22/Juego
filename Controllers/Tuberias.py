import random

class Tuberias:
    def dibujar(self):
        self.tuberia1=self.lienzo.create_rectangle(670, 0, 800, 200, fill=self.color, tags="tuberia" )
        self.tuberia2=self.lienzo.create_rectangle(670, 400, 800, 590, fill=self.color, tags="tuberia" )
        self.decoracion1=self.lienzo.create_rectangle(660, 150, 810, 200, fill=self.color, tags="decoracion")
        self.decoracion2=self.lienzo.create_rectangle(660, 400, 810, 450, fill=self.color, tags="decoracion")



    def __init__(self, lienzo):
        self.lienzo = lienzo
        self.x = 0
        self.y = 0
        self.ancho = 50
        self.alto = 300
        self.color = "#33b812"

        self.dibujar()
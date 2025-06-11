#Manejo del Pajaro y Puntajes

class Manejo_Pajaro:

    def __init__(self,canvas):
        self.lienzo=canvas
        self.velocidad=0
        self.gravedad=2
        self.salto=-15
        self.pajaro = self.lienzo.find_withtag("cuerpo")[0]

    def actualizar_posicion(self):
        self.velocidad +=self.gravedad
        self.mover_pajaro(self.velocidad)
       


    def saltar(self, event=None):
        self.velocidad =self.salto

    def mover_pajaro(self, velocidad):
        self.lienzo.move(self.pajaro, 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ala")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ojo")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("pupila")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("boca")[0], 0, velocidad)




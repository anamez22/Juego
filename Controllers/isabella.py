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
        coords = self.lienzo.coords(self.pajaro)  # [x1, y1, x2, y2]
        _, _, _, y2 = coords #hace que y2 sea la coordenada y del borde inferior del pajaro

    # Evita que baje más allá del suelo 
        if y2 + self.velocidad < 590:
            self.mover_pajaro(self.velocidad)
        else:
            self.velocidad = 0  


    def saltar(self, event=None):
        self.velocidad =self.salto

    def mover_pajaro(self, velocidad):
        self.lienzo.move(self.pajaro, 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ala")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ala_arriba")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ala_abajo")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("ojo")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("pupila")[0], 0, velocidad)
        self.lienzo.move(self.lienzo.find_withtag("boca")[0], 0, velocidad)




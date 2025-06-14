#Manejo del Pajaro y Puntajes

class Manejo_Pajaro:

    def __init__(self,canvas):
        self.lienzo=canvas
        self.velocidad=0
        self.gravedad=2
        self.salto=-15
     

    def actualizar_posicion(self):
        if not getattr(self,"movimiento_activo",True):
            return
        
        self.velocidad += self.gravedad
        coordenadas = self.lienzo.bbox("pajaro") #Posicion del pajaro

        if coordenadas:

            limite_suelo = 590

        if coordenadas[3] + self.velocidad >= limite_suelo:
            # Cuánto falta para llegar al suelo
            desplazamiento = limite_suelo - coordenadas[3]
            self.lienzo.move("pajaro", 0, desplazamiento)
            self.velocidad = 0
        else:
            self.mover_pajaro(self.velocidad)

     
    def detener(self):
        self.movimiento_activo=False

    def saltar(self, event=None):
        self.velocidad =self.salto

    def mover_pajaro(self, velocidad):
        self.lienzo.move("pajaro",0,velocidad)

   




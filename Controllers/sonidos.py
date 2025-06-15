from playsound import playsound
import threading as th
sonido_reproduciendose=False
def reproducir_sonido_juego(ruta):
    global sonido_reproduciendose
    if sonido_reproduciendose:
        return
    sonido_reproduciendose=True

    th.Thread(target=playsound, args=(ruta,),daemon=True).start()
    sonido_reproduciendose=False

def manejar_sonidos(punto=False, gameover=False, vuelo=False):
    if gameover:
        reproducir_sonido_juego("Juego\sonidosFlappy\sonido-muerte.wav")
    elif punto:
        reproducir_sonido_juego("Juego\sonidosFlappy\ganar_punto.wav")

    elif vuelo:
        reproducir_sonido_juego("Juego\sonidosFlappy\sonido_vuelo.wav")
        



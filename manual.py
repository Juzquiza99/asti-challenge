#Librerias
from rrb3 import *
import sys
import tty
import termios
import time
rr = RRB3(5, 4)

#Mapeo de teclas
DELANTE = "w"
ATRAS = "s"
DERECHA = "a"
IZQUIERDA = "d"
SALIDA = "p"

lee2=""

#Funciones para leer el teclado
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  

#Programa principal
try: 
    while True:
        LEER = readkey()
        if LEER == DELANTE:
            print("Arranca")
            rr.forward()
	    while lee2!=DELANTE:
		lee2 = readkey()
                if lee2 == IZQUIERDA:
                    rr.set_motors(0.4,0,1,0)
                    time.sleep(0.3)
		    lee2=""
		    rr.forward()
                if lee2 == DERECHA:
                    rr.set_motors(1,0,0.4,0)
                    time.sleep(0.3)
		    lee2=""
		    rr.forward()
            print("Stop")
            lee2=""
	    rr.stop()
        elif LEER == ATRAS:
            print("Marcha atras")
            rr.reverse()
            while lee2!=ATRAS:
                lee2 = readkey()
                if lee2 == IZQUIERDA:
                    rr.set_motors(0.4,1,1,1)
                    time.sleep(0.3)
                    lee2=""
                    rr.reverse()
                if lee2 == DERECHA:
                    rr.set_motors(1,1,0.4,1)
                    time.sleep(0.3)
                    lee2=""
                    rr.reverse()
            print("Stop")
            lee2=""
	    rr.stop()
        elif LEER == SALIDA:
            raise KeyboardInterrupt
        
#En caso de pulsar la tecla de salida
except KeyboardInterrupt:
    print("Saliendo del programa manual")
    GPIO.cleanup()

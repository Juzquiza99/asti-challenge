#Librerias
from rrb3 import *
import RPi.GPIO as GPIO
import sys
import tty
import termios
import time
rr = RRB3(5, 4)
izquierda = 2
derecha = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(izquierda, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(derecha, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#Mapeo de teclas y sensores
empezar= "w"
salida = "p"

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
        if LEER == empezar:
            print("Arranca")
            rr.forward()
            while lee2 != salida:
        		lee2 = readkey()
        		if GPIO.input(derecha) == GPIO.LOW and GPIO.input(izquierda):
        			rr.forward()
    			if GPIO.input(derecha) == GPIO.HIGH:
    				rr.set_motors(1,0,0.4,0)
    				time.sleep(0.2)
				if GPIO.input(izquierda) == GPIO.HIGH:
					rr.set_motors(0.4,0,1,0)
					time.sleep(0.2)
        elif LEER == salida:
            raise KeyboardInterrupt
    
#En caso de pulsar la tecla de salida
except KeyboardInterrupt:
    print("Saliendo del seguimiento de linea")
    GPIO.cleanup()
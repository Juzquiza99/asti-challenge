#Librerias necesarias
from rrb3 import *
import RPi.GPIO as GPIO
import time
#Voltaje de la placa
rr = RRB3(5, 4)
#Puertos GPIO de los seguidores de linea
izquierda = 2
derecha = 3
#Configuramos los puertos GPIO a utilizar
GPIO.setmode(GPIO.BCM)
GPIO.setup(izquierda, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(derecha, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
#Programa principal
try:
	while True:
		if GPIO.input(derecha) == GPIO.LOW and GPIO.input(izquierda) == GPIO.LOW:
				rr.set_motors(0.5,0,0.5,0)
		elif GPIO.input(derecha) == GPIO.HIGH:
				rr.set_motors(0,0,0.5,0)
				time.sleep(0.05)
		elif GPIO.input(izquierda) == GPIO.HIGH:
				rr.set_motors(0.5,0,0,0)
				time.sleep(0.05)
#Sale del programa con CTRL + C
except KeyboardInterrupt:
	print("Sailendo del seguidor de linea")
	GPIO.cleanup()

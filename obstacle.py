#Librerias
from rrb3 import *
import RPi.GPIO as GPIO
import time
#Voltaje de la placa
rr = RRB3(9, 6)
#Ajuste de los puertos GPIO
GPIO.setmode(GPIO.BCM)

try:
	while True:
		dist = rr.get_distance()
		d = rr.get_distancd()
		i = rr.get_distanci()
		if dist>8:
			rr.set_motors(0.2,0,0.2,0)
		elif dist<8:
			rr.stop()
		elif d<8:
			rr.set_motors(0,0.2,0,0)
			time.sleep(1)
		elif i<8:
			rr.set_motors(0,0,0.2,0)
			time.sleep(1)
			

except KeyboardInterrupt:
	print("Saliendo de obstaculos")
	GPIO.cleanup()
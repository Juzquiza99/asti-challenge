#Librerias
from rrb3 import *
import RPi.GPIO as GPIO
import time
#Voltaje de la placa
rr = RRB3(5, 4)
#Ajuste de los puertos GPIO
GPIO.setmode(GPIO.BCM)

try:
	while True:
		dist = rr.get_distance()
		d = rr.get_distancd()
		i = rr.get_distanci()
		if dist > 20:
			rr.set_motors(0.3,0,0.3,0)
		if dist < 20:
			rr.reverse()
			time.sleep(0.3)
			if rr.get_distanci>rr.get_distancd:
				while True:
					rr.left()
					time.sleep(0.2)
					if rr.get_distance() > 20:
						break

			else:
				while True:
					rr.right()
					time.sleep(0.2)
					if rr.get_distance() > 20:
						break

		if i < 15:
			rr.set_motors(0.3,0,0,0)
			time.sleep(0.1)
		if d < 15:
			rr.set_motors(0,0,0.3,0)
			time.sleep(0.1)
			

except KeyboardInterrupt:
	print("Saliendo de obstaculos")
	GPIO.cleanup()

from rrb3 import *
import RPi.GPIO as GPIO
import time
rr = RRB3(5, 4)
izquierda = 2
derecha = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(izquierda, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(derecha, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
#rr.forward()
#time.sleep(0.2)
while True:
		rr.set_motors(0.2,0,0.2,0)
		if GPIO.input(derecha) == GPIO.LOW and GPIO.input(izquierda) == GPIO.LOW:
			rr.set_motors(0.4,0,0.4,0)
		elif GPIO.input(derecha) == GPIO.HIGH:
			rr.set_motors(0,0,0.4,0)
			time.sleep(0.2)
		elif GPIO.input(izquierda) == GPIO.HIGH:
			rr.set_motors(0.4,0,0,0)
			time.sleep(0.2)

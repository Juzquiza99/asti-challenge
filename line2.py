from rrb3 import *
import RPi.GPIO as GPIO
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
GPIO.setup(14, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

while True:
    rr.set_motors(0.3,0,0.3,0)
	if GPIO.input(derecha) == GPIO.LOW and GPIO.input(izquierda) == GPIO.LOW:
		rr.set_motors(0.3,0,0.3,0)
	elif GPIO.input(derecha) == GPIO.HIGH:
		rr.set_motors(0.3,0,0.1,0)
	elif GPIO.input(izquierda) == GPIO.HIGH:
		rr.set_motors(0.1,0,0.3,0)
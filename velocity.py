#Librerias
from rrb3 import *
rr=RRB3(5, 4)
try:
	while True:
		rr.set_motors(0.9,0,1,0)
		rr.set_oc1(1)
#Al salir del programa, se para el vehiculo y el ventilador propulsor
finally:
	rr.stop()
	rr.set_oc1(0)
	rr.cleanup()
	

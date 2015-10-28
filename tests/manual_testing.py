import requests
import datetime

url = "http://localhost:8000/api/usuario/nuevo"
datos = dict(
    		rpe='790200',
	    	nombre='Rivera Rodriguez Pedro2',
	    	puesto='Gerente',
	    	departamento='Gerencia',
	    	correo='pedro.rivera2@cfe.gob.mx',
	    	registro=str(datetime.datetime.now()),
	    	zona='GTZN'
    		)

r = requests.post(url, data=datos)
#r = requests.get('http://localhost:8000')
if (r.status_code == 200):
	print("Pass!")
	print(r.status_code)
else:
	print("Fail!")
	print(r.status_code)
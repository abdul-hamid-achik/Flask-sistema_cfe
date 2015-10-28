import requests
import datetime
url = "http://localhost:8000/api/usuario/nuevo/"
datos = dict(
    		rpe='79020',
	    	nombre='Rivera Rodríguez Pedro',
	    	puesto='Gerente',
	    	departamento='Gerencia',
	    	correo='pedro.rivera@cfe.gob.mx',
	    	registro=str(datetime.datetime.now()),
	    	zona='GTZN'
    		)

r = requests.post(url, data=datos)

print(r)
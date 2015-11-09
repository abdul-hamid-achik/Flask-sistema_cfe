import requests
import json

url = "http://localhost:5000/"

def testIniciarSesion():
	print("test iniciar sesion: ")
	global url
	print("primero crear usuario nuevo")
	test_url = url + "api/usuarios/nuevo"
	datos = dict(
    		rpe='131231',
	    	nombre='Puerto riquenio',
	    	puesto='Subgerente',
	    	departamento='Gerencia',
	    	correo='puertorico@gmail.com',
	    	zona='GTZN'
    		)
	r = requests.post(test_url, data=datos)
	print(r.status_code)

	print("ahora iniciar sesion")
	test_url = url + "api/sesiones/entrar"

	datos = dict(rpe='131231', correo="puertorico@gmail.com")

	r = requests.post(test_url, data=datos)
	print(r.status_code)

	if r.status_code == 200:
		print("Exitoso!")
	else:
		print("Fracaso!")
		

if __name__ == '__main__':
	testIniciarSesion()
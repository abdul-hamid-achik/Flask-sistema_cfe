import requests
import json

url = "http://localhost:5000/"

def crearUsuarios():
	pass

def testCrearUsuario():
	print("test crear usuario: ")
	global url
	test_url = url + "api/usuario/nuevo"
	datos = dict(
	    		rpe='79020',
		    	nombre='Rivera Rodriguez Pedro',
		    	puesto='Gerente',
		    	departamento='Gerencia',
		    	correo='pedro.rivera2@cfe.gob.mx',
		    	zona='GTZN'
	    		)

	r = requests.post(test_url, data=datos)
	print(r.status_code)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))


def testActualizarUsuario():
	print("test actualizar usuario: ")
	global url
	rpe = '79020'
	test_url = url + "api/usuario/{}/actualizar".format(rpe)
	datos = dict(
	    		rpe='79020',
		    	nombre='Rivera Pedro',
		    	puesto='Sub Gerente',
		    	departamento='Gerencia',
		    	correo='pedro.rivera@cfe.gob.mx',
		    	zona='GTZN'
	    		)
	r = requests.put(test_url, data=datos)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarUsuario():
	print("test consultar usuario en especifico: ")
	global url
	rpe = '79020'
	test_url = url + "api/usuario/{}".format(rpe)

	r = requests.get(test_url)
	print(r.json())
	if isinstance(r.json(), dict):
		print("Exitoso!")
	else:
		print("Fracaso!")

	#datos = dict(
	#    		rpe='79020',
	#	    	nombre='Rivera Pedro',
	#	    	puesto='Sub Gerente',
	#	    	departamento='Gerencia',
	#	    	correo='pedro.rivera@cfe.gob.mx',
	#	    	zona='GTZN'
	#    		)
	#for (k,v) in r.json().items():
	#	print("key: {}, value: {}".format(k,v))
	#	print("comparar valores:")
	#	if datos[k] == v:
	#		pass
	#		#print("es igual")
	#	else:
	#		pass
	#		#print("error en {}: valor = {}, esperado = {}".format(k,v,datos[k]))



def testBorrarUsuario():
	print("test borrar usuario: ")
	global url
	rpe = '79020'
	test_url = url + "api/usuario/{}/borrar".format(rpe)
	r = requests.delete(test_url)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarUsuarios():
	print("test consultar todos los usuarios: ")
	global url
	test_url = url + "api/usuario/todos"
	r = requests.get(test_url)
	if len(r.json()) > 0:
		print("Exitoso!")
	else:
		print("Fracaso!")





if __name__ == '__main__':
	crearUsuarios()

	testCrearUsuario()
	testActualizarUsuario()
	testConsultarUsuario()
	testBorrarUsuario()
	testConsultarUsuarios()
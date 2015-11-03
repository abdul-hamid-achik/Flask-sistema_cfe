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


#Aqui es donde empieza el test de las preguntas

		
def crearPreguntas():
	pass

def testCrearPregunta():
	print("Test para crear preguntas: ")
	global url
	test_url = url + "api/preguntas/nueva"
	datos = dict(
		competencia ='Buena onda',
		pregunta = 'Escoge el que consideres que describe mejor a Abdul Hamid alias abs'
	    )

	r = requests.post(test_url, data=datos)
	print(r.status_code)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))


def testActualizarPreguntas():
	print("Test actualizar la pregunta:")
	global url
	# rpe = '79020'
	id ='1'
	test_url = url + "api/preguntas/{}/actualizar".format(id)
	datos = dict(
	    		competencia= 'Ambicioso/a',
	    		pregunta ='Define tu personalidad:'
	    		)
	r = requests.put(test_url, data=datos)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarPreguntas():
	print("Test consultar una pregunta en especifico:")
	global url
	# rpe = '79020'
	id='4'
	test_url = url + "api/preguntas/{}".format(id)

	r = requests.get(test_url)
	print(r.json())
	if isinstance(r.json(), dict):
		print("Exitoso!")
	else:
		print("Fracaso!")



def testBorrarPreguntas():
	print("Test para borrar la pregunta: ")
	global url
	# rpe = '79020'
	id='4'
	test_url = url + "api/preguntas/{}/borrar".format(id)
	r = requests.delete(test_url)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarPreguntas():
	print("Test para consultar todas las preguntas: ")
	global url
	test_url = url + "api/preguntas/todas"
	r = requests.get(test_url)
	if len(r.json()) > 0:
		print("Exitoso!")
	else:
		print("Fracaso!")		


def crearRespuestas():
	pass

def testCrearRespuesta():
	print("Test para crear respuestas: ")
	global url
	test_url = url + "api/respuestas/nueva"
	datos = dict(
		usuario = 'alejandra',
		pregunta = 'acomoda la competencia en el recuadro adecuado',
		respuesta = 'ambicioso/a'
	    		)

	r = requests.post(test_url, data=datos)
	print(r.status_code)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))


def testActualizarRespuestas():
	print("Test actualizar la respuesta:")
	global url
	# rpe = '79020'
	id ='3'
	test_url = url + "api/respuestas/{}/actualizar".format(id)
	datos = dict(
	    		usuario='alejandra',
	    		pregunta='Escoge lo que creas que peor lo describe',
	    		respuesta='Toma de decisiones'
	    		)
	r = requests.put(test_url, data=datos)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarRespuestas():
	print("Test consultar una respuesta en especifico:")
	global url
	# rpe = '79020'
	id='3'
	test_url = url + "api/respuestas/{}".format(id)

	r = requests.get(test_url)
	print(r.json())
	if isinstance(r.json(), dict):
		print("Exitoso!")
	else:
		print("Fracaso!")


def testBorrarRespuestas():
	print("Test para borrar la respuesta: ")
	global url
	# rpe = '79020'
	id='3'
	test_url = url + "api/respuestas/{}/borrar".format(id)
	r = requests.delete(test_url)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))

def testConsultarRespuestas():
	print("Test para consultar todas las respuestas: ")
	global url
	test_url = url + "api/respuestas/todas"
	r = requests.get(test_url)
	if len(r.json()) > 0:
		print("Exitoso!")
	else:
		print("Fracaso!")




if __name__ == '__main__':
	
	crearUsuarios()
	crearRespuestas()
	crearPreguntas()

	testCrearUsuario()
	testActualizarUsuario()
	testConsultarUsuario()
	testBorrarUsuario()
	testConsultarUsuarios()

	testCrearPregunta()
	testActualizarPreguntas()
	testConsultarPreguntas()
	testBorrarPreguntas()
	testConsultarPreguntas()

	testCrearRespuesta()
	testActualizarRespuestas()
	testConsultarRespuestas()
	testBorrarRespuestas()
	testConsultarRespuestas()






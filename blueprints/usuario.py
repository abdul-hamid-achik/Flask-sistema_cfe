from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Usuario
import json
import datetime

usuario = Blueprint('usuario', __name__ )

@usuario.route('/usuario/todos')
def usuarios_all():
	print(request)
	usuarios = Usuario.select()
	lista_usuarios = [usuario.to_json() for usuario in usuarios]
	return json.dumps(lista_usuarios)

@usuario.route('/usuario/<rpe>')
def usuario_info(rpe):
	print(request)
	try:
		usuario = Usuario.select().where(Usuario.rpe == rpe)
		return json.dumps(usuario[0].to_json()), 200
	except:
		return "Error!", 404

@usuario.route('/usuario/nuevo', methods=['POST'])
def usuario_nuevo():
	print(request)
	try:
		Usuario.nuevo(
	    	rpe=request.form['rpe'],
	    	nombre=request.form['nombre'],
	    	puesto=request.form['puesto'],
	    	departamento=request.form['departamento'],
	    	correo=request.form['correo'],
	    	zona=request.form['zona'])
		return "OK!", 200
	except:
		return "Error!", 404

@usuario.route('/usuario/<rpe>/borrar', methods=['DELETE'])
def usuario_borrar(rpe):
	print(request)
	try:
		usuario = Usuario.select().where(Usuario.rpe == rpe)
		if usuario is not None:
			usuario[0].delete()
			return "OK!", 200
		else:
			return "Error!", 404
	except:
		return "Error!", 404

@usuario.route('/usuario/<rpe>/actualizar', methods=['PUT'])
def usuario_actualizar(rpe):
	print(request)
	try:
		usuario = Usuario.update(
			rpe=request.form['rpe'],
	    	nombre=request.form['nombre'],
	    	puesto=request.form['puesto'],
	    	departamento=request.form['departamento'],
	    	correo=request.form['correo'],
	    	zona=request.form['zona']).where(Usuario.rpe == rpe)
		usuario.execute()
		return "OK!", 200
	except:
		return "Error!", 404
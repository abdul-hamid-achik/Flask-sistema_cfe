from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Usuario
import json
import datetime

usuario = Blueprint('usuario', __name__ )

@usuario.route('/usuario/todos')
def usuarios_all():
	usuarios = Usuario.select()
	lista_usuarios = [usuario.to_json() for usuario in usuarios]
	return json.dumps(lista_usuarios)

@usuario.route('/usuario/<rpe>')
def usuario_info(rpe):
	usuario = Usuario.select().where(Usuario.rpe == rpe)
	return json.dumps(usuario[0].to_json())

@usuario.route('/usuario/nuevo', methods=['POST'])
def usuario_nuevo():
	print("ok")
	print(dir(request))
	Usuario.nuevo(
    	rpe=request.form['rpe'],
    	nombre=request.form['nombre'],
    	puesto=request.form['puesto'],
    	departamento=request.form['departamento'],
    	correo=request.form['correo'],
    	zona=request.form['zona'])#Usuario.get(Usuario.rpe**rpe).to_json()
	return json.dumps("OK!")
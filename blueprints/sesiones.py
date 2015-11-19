#<<<<<<< HEAD
from flask import (Blueprint, request)
import sys
sys.path.append("../Flask-sistema_cfe")
=======
from flask import (Blueprint, request)
#>>>>>>> 0864bffff3f3f5de70af8efd210b25ca9822738b
from models import Usuario
import json
import datetime

sesiones = Blueprint('sesiones', __name__ )

@sesiones.route('/entrar', methods=['POST'])
def sesion_entrar():
  	try:
  		post = request.get_json()
  		usuario = Usuario.select().where((Usuario.rpe == post.get("rpe")) & (Usuario.correo == post.get('correo')))[0]
  		if usuario:
  			return "Ok!", 200
  		else:
  			return "Error!", 404
  	except:
  		return "Error!", 404

@sesiones.route('/salir')
def sesion_salir():
	return "Ok!", 200

@sesiones.route('registrar', methods=['POST'])
def registrar_usuario(self,nombre, correo, rpe, puesto, departamento,zona):
		cls.create(
                nombre=nombre,
                correo=correo,
                rpe=rpe,
                puesto=puesto,
                departamento=departamento,
                zona=zona)



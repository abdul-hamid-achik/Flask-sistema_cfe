from flask import (Blueprint, request) 
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Usuario
import json
import datetime

sesiones = Blueprint('sesiones', __name__ )

@sesiones.route('/entrar', methods=['POST'])
def sesion_entrar():
  	try:
  		usuario = Usuario.select().where((Usuario.rpe == request.form["rpe"]) & (Usuario.correo == request.form['correo']))[0]
  		if usuario:
  			return "Ok!", 200
  		else:
  			return "Error!", 404
  	except:
  		return "Error!", 404


@sesiones.route('/salir')
def sesion_salir():
	return "Ok!", 200



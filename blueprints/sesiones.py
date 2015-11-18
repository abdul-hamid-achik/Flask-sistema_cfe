from flask import (Blueprint, request)
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



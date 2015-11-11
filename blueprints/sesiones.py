from flask import (Blueprint, request) 
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
import json
import datetime

sesiones = Blueprint('sesiones', __name__ )

@sesiones.route('/iniciar_sesion', methods=['POST'])
def sesion_entrar():
	
  	


@sesiones.route('/cerra_sesion')
def sesion_salir():
	pass



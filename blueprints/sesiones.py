from flask import (Blueprint, request) 
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
import json
import datetime

sesiones = Blueprint('sesiones', __name__ )

@sesiones.route('/login', methods=['POST'])
def sesion_entrar():
    pass


@sesiones.route('/logout')
def sesion_salir():
	pass



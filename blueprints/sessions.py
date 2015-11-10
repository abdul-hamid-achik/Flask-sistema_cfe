from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
import json
import datetime

sessiones = Blueprint('sessiones', __name__ )

@sessiones.route('/login')
def session_iniciar():
	pass

@sessiones.route('/logout')
def session_cerrar():
	pass


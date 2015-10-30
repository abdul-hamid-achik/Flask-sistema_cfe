from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Respuestas
import json
import datetime

respuestas = Blueprint('respuestas', __name__ )

@respuestas.route('/todos')
def respuestas_todas():
	pass

@respuestas.route('/nueva', methods=['POST'])
def respuestas_nueva():
	pass
	
@respuestas.route('/<int:id>')
def respuestas_info(id):
	pass

@respuestas.route('/<int:id>/borrar', methods=['DELETE'])
def respuestas_borrar(id):
	pass

@respuestas.route('/<int:id>/actualizar', methods=['PUT'])
def respuestas_actualizar(id):
	pass

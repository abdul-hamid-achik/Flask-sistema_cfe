from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Preguntas
import json
import datetime

preguntas = Blueprint('preguntas', __name__ )

@preguntas.route('/todos')
def preguntas_todas():
	pass

@preguntas.route('/nueva', methods=['POST'])
def preguntas_nueva():
	pass
	
@preguntas.route('/<int:id>')
def preguntas_info(id):
	pass

@preguntas.route('/<int:id>/borrar', methods=['DELETE'])
def preguntas_borrar(id):
	pass

@preguntas.route('/<int:id>/actualizar', methods=['PUT'])
def preguntas_actualizar(id):
	pass

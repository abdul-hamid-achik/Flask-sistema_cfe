from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Respuestas
import json
import datetime

respuestas = Blueprint('respuestas', __name__ )

@respuestas.route('/todas')
def respuestas_todas():
	respuestas = Respuestas.select()
	lista_respuestas = [respuesta.to_json() for respuesta in respuestas]
	return json.dumps(lista_respuestas)


@respuestas.route('/nueva', methods=['POST'])
def respuestas_nueva():
	try:
		respuesta = Respuestas.create(
			usuario = usuario.form['usuario'], #id de el usuario que pone la respuesta
			pregunta = pregunta.form['pregunta'], #id de pregunta
			respuesta = respuesta.form['respuesta'])
		return "OK", 200
	except:
		return "Error!", 404
			
	
@respuestas.route('/<int:id>')
def respuestas_info(id):
	try:
		respuesta = Respuestas.select().where(Respuesta.id == id)
		return json.dumps(respuesta(0).to_json()), 200
	except:
		return "Error!", 404


@respuestas.route('/<int:id>/borrar', methods=['DELETE'])
def respuestas_borrar(id):
	try:
		respuesta = Respuestas.select().where(Respuestas.id == id)
		if respuesta is not None:
			respuesta[0].delete()
			return "Se ha eliminado", 200
		else:
			return "Error!", 404
	except:
		return "Error", 404		

@respuestas.route('/<int:id>/actualizar', methods=['PUT'])
def respuestas_actualizar(id):
	try:
		respuesta = Respuestas.update(
			usuario = request.form['usuario'],
			pregunta = request.form['pregunta'],
			respuesta = request.form['respuesta']
			).where(Respuestas.id == id)
		respuestas.execute()
		return "Ok!", 200
	except:
		return "Error", 404


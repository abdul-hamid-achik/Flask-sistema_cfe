from flask import Blueprint, request
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
from models import Preguntas
import json
import datetime

preguntas = Blueprint('preguntas', __name__ )

@preguntas.route('/todas')
def preguntas_todas():
	preguntas= Preguntas.select()
	lista_preguntas= [preguntas.to_json() for pregunta in preguntas]
	return json.dumps(listas_preguntas)

@preguntas.route('/nueva', methods=['POST'])
def preguntas_nueva():
	try: 
		pregunta = Preguntas.create(
			competencia = request.form['competencia'],
			pregunta = request.form['pregunta']
			)
	return "OK!", 200
	except:
	return "ERROR", 404		
	
@preguntas.route('/<int:id>')
def preguntas_info(id):
	try: 
		pregunta = Preguntas.select().where(Preguntas.id == id)
	return json.dumps(pregunta(0).to_json()),200
    except:
    	return "Error!", 404

@preguntas.route('/<int:id>/borrar', methods=['DELETE'])
def preguntas_borrar(id):
	try:
		pregunta = Preguntas.select().where(Preguntas.id == id)
		if pregunta is not None:
			pregunta(0).delete()
			return "OK", 200
		else:
			return "Error!", 404
		except:
			return "Error!", 404	

@preguntas.route('/<int:id>/actualizar', methods=['PUT'])
def preguntas_actualizar(id):
	try:
		pregunta = Preguntas.update(
			competencia = request.form['competencia'],
			pregunta = request.form['pregunta']
			).where(Preguntas.id == id)
		respuesta.execute()
		return "Ok!", 200
	except:
		return "Error!", 404

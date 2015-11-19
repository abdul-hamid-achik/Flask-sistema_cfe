from flask import Blueprint, request
import sys
# sys.path.insert(0, '~/Projects/Flask-sistema_cfe')
sys.path.append("../Flask-sistema_cfe")
from models import Competencias
import json
import datetime

competencias = Blueprint('competencias', __name__ )

@competencias.route('/todas')
def competencias_todas():
	competencias = Competencias.select()
	listas_competencias = [competencia.to_json() for competencia in competencias]
	return json.dumps(listas_competencias)

@competencias.route('/<id>')
def competencia_info(id):
	try:
		competencia = Competencias.select().where(Competencias.id == id)[0]
		return json.dumps(competencia.to_json()), 200
	except:
		return "Error!", 404

@competencias.route('/nueva', methods=['POST'])
def competencia_nueva():
	try:
		competencia = Competencias.create(
			nombre = request.form['nombre'],
			descripcion = request.form['descripcion'])
		return "OK!", 200
	except:
		return "Error!", 404

@competencias.route('/<id>/actualizar', methods=['PUT'])
def competencia_actualizar(id):
	try:
		competencia = Competencias.update(
				nombre = request.form['nombre'],
				descripcion = request.form['descripcion']
			).where(Competencias.id == id)
		competencia.execute()
		return "OK!", 200
	except: 
		return "Error!", 404

@competencias.route('/<id>/borrar', methods=['DELETE'])
def competencia_borrar(id):
	try:
		competencia = Competencias.select().where(Competencias.id == id)
		if competencia is not None:
			competencia[0].delete()
			return "OK!", 200
		else:
			return "Error!", 404
	except:
		return "Error!", 404
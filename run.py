from flask import (Flask, g, render_template, flash, redirect, url_for, request, make_response, jsonify)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask.ext.bcrypt import check_password_hash
import forms
import models
from werkzeug import secure_filename
import os
import json

DEBUG = True
PORT = 8000
HOST = '127.0.0.1'
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static/media/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'daniela_omg'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'

@login_manager.user_loader
def cargar_usuario(usuarioid):
    try:
        return models.Usuario.get(models.Usuario.id == usuarioid)
    except models.DoesNotExist:
        return None


@app.before_request
def antes_request():
	"""Conectarse a la base de datos """
	g.db = models.DATABASE
	g.db.connect()
	g.user = current_user



@app.after_request
def despues_request(response):
	"""Cerrar la conexion despues de cada request"""
	g.db.close()
	return response


@app.route('/')
def main():
	usuario=g.user._get_current_object()
	#return make_response(open('templates/index.html').read())
	return render_template('index.html')


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
	usuario = models.Usuario.get(models.Usuario.correo**request.form['correo'])
	if request.form['password'] == usuario.rpe:
		login_user(usuario)
		return redirect(url_for('seleccionar_colegas'))


@app.route('/usuario')
@login_required
def get_usuario():
	return json.dumps(g.user._get_current_object().to_json())


@app.route('/sistema')
@login_required
def sistema():
	return make_response(open('templates/sistema.html').read())



####
####    seleccionar a los que te permitiran evaluarlos
####

@app.route('/seleccionar_colegas')
@login_required
def seleccionar_colegas():

	return make_response(open('templates/seleccionar_colegas.html').read())

@app.route('/colegas')
@login_required
def colegas():
	usuarios = models.Usuario.select().where(
		(models.Usuario.puesto==g.user.puesto) &
		(models.Usuario.id != g.user.id) )
	colegas = list()
	for usuario in usuarios:
		colegas.append(usuario.to_json())
	return json.dumps(colegas)

@app.route('/get_colegas_evaluar')
@login_required
def get_colegas():
	evaluadores = models.Usuario.get(models.Usuario.id**g.user._get_current_object().id)
	colegas = list()
	for evaluador in evaluadores.evaluan():
		colegas.append(evaluador.to_json())
	return json.dumps(colegas)

@app.route('/get_subordinados')
@login_required
def get_subordinados():
	usuario = g.user._get_current_object()
	subordinados = list()
	for subordinado in usuario.subordinados():
		subordinados.append(subordinado.to_json())
	return json.dumps(subordinados)

@app.route('/get_superiores')
@login_required
def get_superiores():
	usuario = g.user._get_current_object()
	superiores = list()
	for superior in usuario.superiores():
		superiores.append(superior.to_json())
	return json.dumps(superiores)

@app.route('/puede_evaluarme', methods=['POST'])
@login_required
def puede_evaluarme():
	colega = request.get_json()
	get_modelo = models.Usuario.get(models.Usuario.nombre**colega['nombre'])
	models.PermisoEvaluar.create(
		evaluado=g.user._get_current_object(),
		evaluador=get_modelo
		)
	string = "{} ahora podra ser evaluada por {}".format(g.user.nombre, colega['nombre'])
	return json.dumps({'response': string})

@app.route('/numero_evaluadores')
@login_required
def numero_evaluadores():
	numero = models.PermisoEvaluar.select().where(models.PermisoEvaluar.evaluado==g.user._get_current_object()).count()
	ids = models.PermisoEvaluar.select().where(models.PermisoEvaluar.evaluado==g.user._get_current_object())

	lista_ids = list()
	for Id in ids:
		lista_ids.append(Id.evaluador.rpe)
	return json.dumps({
	                  "cantidad": numero,
	                  "seleccionados": lista_ids,
	                  })

@app.route('/evaluando', methods=['POST'])
@login_required
def evaluando():
	evaluacion = request.get_json()
	usuario = g.user._get_current_object()
	colega = models.Usuario.get(models.Usuario.nombre**evaluacion['colega']['nombre'])
	competencia = models.Competencias.get(models.Competencias.nombre**evaluacion['competencia']['nombre'])
	tipo = models.TipoCompetencia.get(models.TipoCompetencia.nombre**evaluacion['tipo'])
	models.Evaluando.nuevo(
		empleado=usuario,
		colega=colega,
		competencia=competencia,
		tipo=tipo
		)

	return json.dumps(
		{
		"response" : "{} evaluo a {} decidiendo que la competencia: {} es {}".format(
			usuario.nombre, colega.nombre, competencia.nombre, tipo.nombre)
		}
	)

@app.route('/evaluando_neutras', methods=['POST'])
@login_required
def evaluando_neutras():	

	evaluacion = request.get_json()

	for competencia in evaluacion['competencias']:
		usuario = g.user._get_current_object()
		colega = models.Usuario.get(models.Usuario.nombre**evaluacion['colega']['nombre'])
		competencia = models.Competencias.get(models.Competencias.nombre**competencia['nombre'])
		tipo = models.TipoCompetencia.get(models.TipoCompetencia.nombre**'Neutras')
		
		models.Evaluando.nuevo(
			empleado=usuario,
			colega=colega,
			competencia=competencia,
			tipo=tipo

			)
	return "ok"


@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
	logout_user()
	flash('Haz salido de la sesion exitosamente!', 'success')
	return redirect(url_for('main'))


@app.route('/get_competencias')
@login_required
def get_competencias():
	competencias = models.Competencias.select()
	lista_competencias = list()
	for competencia in competencias:
		lista_competencias.append(competencia.to_json())
	return json.dumps(lista_competencias)

@app.route('/get_competencias/existentes', methods=['POST'])
@login_required
def existentes():
	respuesta = list()
	resultados = list()
	peticion = request.get_json()
	empleado = g.user._get_current_object()
	tipo = models.TipoCompetencia.get(models.TipoCompetencia.nombre ** peticion['tipo'])
	colega = models.Usuario.get(models.Usuario.nombre**peticion['colega']['nombre'])
	evaluaciones = models.Evaluando.select().where(
	    (models.Evaluando.empleado == g.user._get_current_object()) &
		(models.Evaluando.colega == colega) &
		(models.Evaluando.tipo == tipo)
		)
	for evaluacion in evaluaciones:
		resultados.append(models.Competencias.get(models.Competencias.id**evaluacion.competencia))
	for resultado in resultados:
		respuesta.append(resultado.to_json())
	return json.dumps(respuesta)


@app.route('/get_competencias/inexistentes', methods=['POST'])
@login_required
def inexistentes():
	respuesta = list()
	resultados = list()
	peticion = request.get_json()
	empleado = g.user._get_current_object()
	tipo = models.TipoCompetencia.get(models.TipoCompetencia.nombre ** peticion['tipo'])
	colega = models.Usuario.get(models.Usuario.nombre**peticion['colega']['nombre'])
	evaluaciones = models.Evaluando.select().where(
	    (models.Evaluando.empleado == g.user._get_current_object()) &
		(models.Evaluando.colega == colega) &
		(models.Evaluando.tipo == tipo)
		)
	for evaluacion in evaluaciones:
		resultados.append(models.Competencias.get(models.Competencias.id**evaluacion.competencia))
	for resultado in resultados:
		respuesta.append(resultado.to_json())
	return json.dumps(respuesta)


@app.route('/get_competencias/neutras', methods=['POST'])
@login_required
def neutras():
	respuesta = list()
	resultados = list()
	peticion = request.get_json()
	existente = models.TipoCompetencia.get(models.TipoCompetencia.nombre ** 'Existentes')
	inexistente = models.TipoCompetencia.get(models.TipoCompetencia.nombre ** 'Inexistentes')

	colega = models.Usuario.get(models.Usuario.nombre**peticion['colega']['nombre'])
	evaluaciones_inexistentes = models.Evaluando.select().where(
	    (models.Evaluando.empleado == g.user._get_current_object()) &
		(models.Evaluando.colega == colega) &
		(models.Evaluando.tipo == inexistente)
		)
	evaluaciones_existentes = models.Evaluando.select().where(
	    (models.Evaluando.empleado == g.user._get_current_object()) &
		(models.Evaluando.colega == colega) &
		(models.Evaluando.tipo == existente)
		)
	for evaluacion in evaluaciones_existentes:
		resultados.append(models.Competencias.get(models.Competencias.id**evaluacion.competencia))

	for evaluacion in evaluaciones_inexistentes:
		resultados.append(models.Competencias.get(models.Competencias.id**evaluacion.competencia))

	for resultado in resultados:
		respuesta.append(resultado.to_json())

	return json.dumps(respuesta)

@app.route('/reporte')
@login_required
def reporte():

	### obtener todas las competencias evaluadas

	evaluaciones = models.Evaluando.select().where(models.Evaluando.colega==g.user._get_current_object())
	for evaluacion in evaluaciones:
		
		print("{} evaluo a {} con la competencia {} decidiendo que es {} en su persona".format(
			evaluacion.empleado, 
			evaluacion.colega,
			evaluacion.competencia, 
			evaluacion.tipo)
		)
		print("numero de {} en {}".format(evaluacion.competencia, evaluacion.colega))

		print(evaluacion.competencia.get_numero_por_usuario(
			evaluacion.colega
			)
		)

		print("numero de {} ".format(evaluacion.tipo))

		print(
			evaluacion.tipo.numero_tipo_competencia(
				evaluacion.colega, 
				evaluacion.competencia
				)
			)

	lista_datos = [ {
		"evaluador": evaluacion.empleado.to_json(),
		"evaluado": evaluacion.colega.to_json(),
		"competencia" : evaluacion.competencia.to_json(),
		"tipo" :evaluacion.tipo.to_json(),
		"cantidad" : evaluacion.competencia.get_numero_por_usuario(evaluacion.colega),
		"cantidad_por_tipo": evaluacion.tipo.numero_tipo_competencia(evaluacion.competencia, evaluacion.colega)
	} for evaluacion in evaluaciones]
	#lista_datos = list()
	#for dato in datos:
	#	lista_dato = {
	#	"evaluador" : dato.empleado.to_json(),
	#	"evaluado" : dato.colega.to_json(),
	#	"competencia" : dato.competencia.to_json(),
	#	"tipo" : dato.tipo.to_json()
	#	}
	#	lista_datos.append(lista_dato)

	#return json.dumps(lista_datos)
	return json.dumps(lista_datos)

@app.route('/resultados')
@login_required
def resultados():
	return make_response(open('templates/reportes.html').read())
if __name__ == '__main__':
	models.initialize()
	app.run(
    	debug=DEBUG,
    	port=PORT,
    	host=HOST
    )

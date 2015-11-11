from flask import (Flask, g, render_template, flash, redirect, url_for, request, make_response, jsonify)
from flask.ext.login import (LoginManager, login_user, logout_user, login_required, current_user)
from flask.ext.bcrypt import check_password_hash
from blueprints.usuarios import usuarios
from blueprints.competencias import competencias
from blueprints.preguntas import preguntas
from blueprints.respuestas import respuestas
import models
from werkzeug import secure_filename
import os
import json
import ast
DEBUG = True
PORT = 5000
HOST = '127.0.0.1'
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/static/media/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'niggersan'
app.register_blueprint(usuarios, url_prefix='/api/usuarios')
app.register_blueprint(competencias, url_prefix='/api/competencias')
app.register_blueprint(preguntas, url_prefix='/api/preguntas')
app.register_blueprint(respuestas, url_prefix='/api/respuestas')
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


@app.route('/usuario')
@login_required
def get_usuario():
	return json.dumps(g.user._get_current_object().to_json())


####
####    seleccionar a los que te permitiran evaluarlos
####

@app.route('/seleccionar_colegas')
@login_required
def seleccionar_colegas():

	return render_template('seleccionar_colegas.html')

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

@app.route('/registrarUsuario', methods['POST'])
def registrarUsuario():
	models.Usuario.nuevo()
	    	rpe=request.form['rpe'],
	    	nombre=request.form['nombre'],
	    	puesto=request.form['puesto'],
	    	departamento=request.form['departamento'],
	    	correo=request.form['correo'],
	    	zona=request.form['zona'])
		)


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
	print(request.form['correo'])
	usuario = models.Usuario.get(models.Usuario.correo**request.form['correo'])
	if request.form['password'] == usuario.rpe:
		session['login_user(usuario)']=True
		status= True
		return 'Login successfull'
	else:
		status = False
		return 'Login failed.'
		

# 


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

@app.route('/reportes')
@login_required
def reportes():
	competencias = models.Competencias.select()
	tipocompetencia = models.TipoCompetencia.select()
	datos = { 
		"nombre" : g.user._get_current_object().nombre, 
		"competencias": [ 
		{
			"nombre": competencia.nombre,
			"numero" : competencia.get_numero_por_usuario(g.user._get_current_object()),
			"tipo": [{
				"nombre": tipo.nombre,
				"numero": tipo.numero_tipo_competencia(competencia,g.user._get_current_object())
			} for tipo in tipocompetencia
			]
		} for competencia in competencias
		]
	}
	return json.dumps(datos)

@app.route('/get_preguntas', methods=['POST'])
@login_required
def get_preguntas():
	competencia =  models.Competencias.select().where(models.Competencias.nombre == request.get_json()['nombre']).get()
	return json.dumps(competencia.preguntas())

@app.route('/respuestas_preguntas', methods=['POST'])
@login_required
def respuestas_preguntas():
	print(request.form)
	return "ok"
	
if __name__ == '__main__':
	#models.drop()
	
	models.initialize()
	app.run(
    	debug=DEBUG,
    	port=PORT,
    	host=HOST
    )

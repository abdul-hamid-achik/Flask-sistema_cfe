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
login_manager.login_view = 'iniciar_sesion'

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
	print(request)
	usuario = models.Usuario.get(models.Usuario.correo**request.form['correo'])
	if request.form['password'] == usuario.rpe:
		login_user(usuario)
		return redirect(url_for('seleccionar_colegas'))


@app.route('/sistema')
@login_required
def sistema():
	return make_response(open('templates/sistema.html').read())

@app.route('/seleccionar_colegas')
@login_required
def seleccionar_colegas():

	return make_response(open('templates/seleccionar_colegas.html').read())

@app.route('/colegas')
@login_required
def get_colegas():
	usuarios = models.Usuario.select().where(models.Usuario.departamento**g.user.departamento)
	colegas = list()
	for usuario in usuarios:
		colegas.append(usuario.to_json())
	return json.dumps(colegas) 

@app.route('/puede_evaluarme', methods=['POST'])
@login_required
def puede_evaluarme():
	colega = request.get_json()
	get_modelo = models.Usuario.get(models.Usuario.nombre**colega['nombre'])
	models.Evalua.create( 
		evaluado=g.user._get_current_object(),
		evaluador=get_modelo
		)
	print(models.Evalua.get(models.Evalua.evaluado**g.user._get_current_object()))
	string = "{} ahora podra ser evaluada por {}".format(g.user.nombre, colega['nombre'])
	return json.dumps({'response': string})


@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
	logout_user()
	flash('Haz salido de la sesion exitosamente!', 'success')
	return redirect(url_for('main'))


if __name__ == '__main__':
	models.initialize()
	
	app.run(
    	debug=DEBUG, 
    	port=PORT, 
    	host=HOST
    )
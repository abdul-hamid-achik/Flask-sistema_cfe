from flask import (Blueprint, request, session,redirect, url_for, escape) 
import sys
sys.path.insert(0, '/Users/alemv18/Desktop/Flask-sistema_cfe-master/')
import json
import datetime

sessiones = Blueprint('sessiones', __name__ )

@sessiones.route('/login')
def session_iniciar():
    if 'usuario' in session:
        return 'Se ha iniciado sesión como: %s' % escape(session['usuario'])
    return 'No se ha podido ingresar'

@app.route('/login', methods=['GET', 'POST'])
def session_cerrar():
    if request.method == 'POST':
        session['usuario'] = request.form['usuario']
        return redirect(url_for('index'))
  
@app.route('/logout')
def logout():
    # quitar al usuario de la sesión si ya no esta conectado
    session.pop('usuario', None)
    return redirect(url_for('index'))



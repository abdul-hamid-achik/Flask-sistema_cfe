import datetime
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from peewee import *

# no funciona aun no esta listo esto usar _models.py en su lugar
from competencia import *
from evaluacion import *
from jerarquia import *
from pregunta import *
from respuesta import *
from tipocompetencia import *
from usuario import *

DATABASE = SqliteDatabase('../sistema_cfe.db')
import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from peewee import *

DATABASE = MySQLDatabase('sistema_cfe', user='root', password='aa121292')

class Usuario(UserMixin, Model):
    rpe = CharField(unique=True)
    nombre = CharField(max_length=100)
    puesto = CharField(max_length=100)
    departamento = CharField(max_length=100)
    correo = CharField(unique=True)
    registro = DateTimeField(default=datetime.datetime.now)
    admin = BooleanField(default=False)
   
    class Meta:
        database = DATABASE
        order_by = ('-registro',)

    @classmethod
    def nuevo(cls, rpe, nombre, puesto, departamento, correo, admin=False):
    	try:
    		cls.create(
	    		rpe=rpe,
	    		nombre=nombre,
	    		puesto=puesto,
	    		departamento=departamento,
	    		correo=correo,
	    		admin=admin	    		
	    	)
    	except IntegrityError:
    		raise ValueError("El usuario ya existe")

    def __repr__(self):
    	return '{}'.format(self.nombre)

    def to_json(self):
    	return { 
    	"rpe" : self.rpe,
    	"nombre" : self.nombre,
    	"puesto": self.puesto,
    	"departamento": self.departamento,
    	"correo": self.correo,
    	"admin": self.admin
    	}

class Evalua(Model):
	evaluado = ForeignKeyField(Usuario, related_name='evaluado')
	evaluador = ForeignKeyField(Usuario, related_name='evaluador')

	class Meta:
		database = DATABASE
		indexes = (
			(('evaluado','evaluador'), True),
		)
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Usuario, Evalua], safe=True)
    DATABASE.close()

def drop():
	DATABASE.connect()
	DATABASE.drop_tables([Usuario, Evalua], safe=True)
	DATABASE.close()
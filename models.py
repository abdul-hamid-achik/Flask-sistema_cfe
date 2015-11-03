import datetime
from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
from peewee import *
import sys
sys.path.insert(0, '~/Projects/Flask-sistema_cfe')

DATABASE = SqliteDatabase('sistema_cfe.db')

class Usuario(UserMixin, Model):
    rpe = CharField(unique=True)
    nombre = CharField(max_length=100)
    puesto = CharField(max_length=100)
    departamento = CharField(max_length=100)
    correo = CharField(unique=True)
    registro = DateTimeField(default=datetime.datetime.now)
    #admin = BooleanField(default=False)
    zona = CharField(max_length=20)

    class Meta:
        database = DATABASE
        order_by = ('-registro',)

    @classmethod
    def nuevo(cls, rpe, nombre, puesto, departamento, correo, zona):
        try:
            cls.create(
                rpe=rpe,
                nombre=nombre,
                puesto=puesto,
                departamento=departamento,
                correo=correo,
                zona=zona
            )
        except IntegrityError:
            raise ValueError("El usuario ya existe")

    def __repr__(self):
        return '{}'.format(self.nombre)

    def to_json(self):
        return {
            "rpe": self.rpe,
            "nombre": self.nombre,
            "puesto": self.puesto,
            "departamento": self.departamento,
            "correo": self.correo,
            #"admin": self.admin,
            "zona": self.zona
        }

    def evaluan(self):
        return (
            Usuario.select().join(
                PermisoEvaluar, on=PermisoEvaluar.evaluado).where(
                PermisoEvaluar.evaluador == self)
        )

    def evalua(self):
        return (
            Usuario.select().join(
                Evalua, on=Evalua.evaluador).where(
                Evalua.evaluado == self)
        )

    def superiores(self):
        puesto = Jerarquia.get(Jerarquia.nombre**self.puesto)
        return (
            Usuario.select().where(Usuario.puesto**puesto.superior)
        )

#
# sin tomar encuenta la zona o el departamento todavia
#

    def subordinados(self):
        puesto = Jerarquia.get(Jerarquia.superior**self.puesto)
        return (
            Usuario.select().where(Usuario.puesto**puesto.nombre)
        )


class PermisoEvaluar(Model):
    evaluado = ForeignKeyField(Usuario, related_name='evaluado')
    evaluador = ForeignKeyField(Usuario, related_name='evaluador')

    class Meta:
        database = DATABASE
        indexes = (
            (('evaluado', 'evaluador'), True),
        )

    def to_json(self):
        return {
            "evaluado" : self.evaluado,
            "evaluador" : self.evaluador
            }


class Competencias(Model):
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=500)

    class Meta:
        database = DATABASE


    def get_numero_por_usuario(self, usuario):
        evaluacion = Evaluando.select().where(Evaluando.colega == usuario, Evaluando.competencia == self.id).count()
        return evaluacion


    def to_json(self):
        return {
        "nombre" : self.nombre,
        "descripcion" : self.descripcion
        }

    def preguntas(self):
        preguntas = Preguntas.select().where(Preguntas.competencia == self.id)
        lista = [pregunta.to_json() for pregunta in preguntas]
        return lista

    def __repr__(self):
        return self.nombre


class Preguntas(Model):
    competencia = ForeignKeyField(Competencias)
    pregunta = CharField(max_length=500)

    class Meta:
        database = DATABASE

    @classmethod
    def nueva(cls, competencia, pregunta):
        cls.create(
                competencia=competencia,
                pregunta=pregunta
        )
    def to_json(self):
        return {
            "pregunta" : self.pregunta
        }
    def get_respuestas(self):
        respuestas = Respuestas.select().where(Respuestas.pregunta == self.id)
        return respuestas

    def __repr__(self):
        return self.pregunta


class Respuestas(Model):
    usuario = ForeignKeyField(Usuario)
    pregunta = ForeignKeyField(Preguntas)
    respuesta = BooleanField()

    class Meta:
        database = DATABASE

    @classmethod
    def nueva(cls, usuario, pregunta, respuesta):
        cls.create(
            usuario=usuario,
            pregunta=pregunta,
            respuesta=respuesta
        )



class TipoCompetencia(Model):
    nombre = CharField(max_length=50)

    class Meta:
        database = DATABASE


    def to_json(self):
        return {
        "nombre" : self.nombre
        }


    def __repr__(self):
        return self.nombre

    def numero_tipo_competencia(self, competencia, usuario):

        tipo = Evaluando.select().where(
            Evaluando.colega == usuario,
            Evaluando.competencia == competencia,
            Evaluando.tipo == self.id
            ).count()
        return tipo


class Evaluando(Model):
    empleado = ForeignKeyField(Usuario, related_name='empleado')
    colega = ForeignKeyField(Usuario, related_name='colega')
    competencia = ForeignKeyField(Competencias, related_name='competencia')
    tipo = ForeignKeyField(TipoCompetencia, related_name='tipo')


    class Meta:
        database = DATABASE
        indexes = (
            (('empleado','colega', 'tipo', 'competencia'), True),
        )


    def to_json(self):
        return {
        "evaluador":self.empleado,
        "evaluado": self.colega,
        "competencia": self.competencia,
        "tipo": self.tipo
        }


    @classmethod
    def nuevo(cls, empleado, colega, competencia, tipo):
        try:
            cls.create(
                empleado=empleado,
                colega=colega,
                competencia=competencia,
                tipo=tipo
                )
        except IntegrityError:
            raise ValueError("ya se realizo esta evaluacion")




class Jerarquia(Model):
    nombre = CharField(max_length=100)
    superior = CharField(max_length=100)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([
        Usuario,
        PermisoEvaluar,
        Competencias,
        Evaluando,
        TipoCompetencia,
        Jerarquia,
        Preguntas,
        Respuestas], safe=True)
    DATABASE.close()

def drop():
    DATABASE.connect()
    DATABASE.drop_tables([
        Usuario,
        PermisoEvaluar,
        Competencias,
        Evaluando,
        TipoCompetencia,
        Jerarquia,
        Preguntas,
        Respuestas], safe=True)
    DATABASE.close()

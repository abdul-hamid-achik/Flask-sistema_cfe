from __init__ import *

class Competencia(Model):
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=500)

    class Meta:
        database = DATABASE


    def get_numero_por_usuario(self, usuario):
        evaluacion = Evaluacion.select().where(Evaluacion.colega == usuario, Evaluacion.competencia == self.id).count()
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
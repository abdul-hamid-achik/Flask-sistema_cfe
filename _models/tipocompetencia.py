from __init__ import *

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

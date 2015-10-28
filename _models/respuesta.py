from __init__ import *

class Respuesta(Model):
    usuario = ForeignKeyField(Usuario)
    pregunta = ForeignKeyField(Pregunta)
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


from __init__ import *

class Jerarquia(Model):
    nombre = CharField(max_length=100)
    superior = CharField(max_length=100)
    # empleado = CharField(max_length=100)
    # colega = CharField(max_length=100)

    class Meta:
        database = DATABASE

 @classmethod
    def nueva(cls, nombre, superior):
        cls.create(
                nombre=nombre
                superior=superior

        )
    def to_json(self):
        return {
            "nombre" : self.nombre
            "superior" : self.superior
        }

    # def get_jerarquia(self):
    #     jerarquia = Respuesta.select().where(Respuesta.pregunta == self.id)
    #     return respuestas

    # def __repr__(self):
    #     return self.pregunta9        

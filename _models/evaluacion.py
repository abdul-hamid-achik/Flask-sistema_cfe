from __init__ import *

class Evaluacion(Model):
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


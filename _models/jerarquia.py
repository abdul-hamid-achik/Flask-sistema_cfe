from __init__ import *

class Jerarquia(Model):
    nombre = CharField(max_length=100)
    superior = CharField(max_length=100)

    class Meta:
        database = DATABASE
import os
# 1 para desarrollo y 0 para pruebas
os.environ['DB'] = '0'

def select_database(var):
	if var == '0':
		return ''
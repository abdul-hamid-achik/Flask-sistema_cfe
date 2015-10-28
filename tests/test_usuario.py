import sys
sys.path.insert(0, '/home/abdul/Projects/Flask-sistema_cfe')
from run import app
import unittest
import json
import datetime
class FlaskUsuarioTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 


    def test_nuevo_usuario(self):
        # sends HTTP POST request to the application
        # on the specified path 
        datos = dict(
        		rpe='79020',
		    	nombre='Rivera Rodríguez Pedro',
		    	puesto='Gerente',
		    	departamento='Gerencia',
		    	correo='pedro.rivera@cfe.gob.mx',
		    	registro=str(datetime.datetime.now()),
		    	zona='GTZN'
        		)
        response = self.app.post('/api/usuario/nuevo/', data=datos, content_type='application/json')
        # assert the response data
        self.assertEqual(response.data, "OK!") 

if __name__ == '__main__':
    unittest.main()
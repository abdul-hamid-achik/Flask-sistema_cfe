import os.path
# import os
import flaskr
import unittest

# import tempfile

class pruebaSesiones(unittest.TestCase):


  def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
    	rv= self.app.get('/')
    	assert 'No entries here so far' in rv.data

    def iniciar_sesion(self, rpe, correo):
    		return self.app.post('/iniciar_sesion', data = dict(
    			rpe=rpe, 
    			correo=correo
    			), follow_redirects=True)

    def cerrar_sesion(self):
    	return self.app.get('/cerrar_sesion',follow_redirects=True)

    def test_sesion_cerrar(self):
    	rv= self.iniciar_sesion('1231278','alejandra munoz',
    		'subordinada', 'calidad','alemv18@gmail.com','norte')
    		assert 'OK!' in rv.data
    	rv = self.cerrar_sesion()
    	assert 'Error!' in rv.data

    def 	






if __name__ == '__main__' :
		test.main()
		unittest.main()


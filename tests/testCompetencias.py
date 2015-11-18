import requests
import json

url = "http://localhost:5000/"

def testCrearCompetencias():
	print("test crear competencias: ")
	global url
	test_url = url + "api/competencias/nueva"
	for i in range(0, 60):
		r = requests.post(test_url, data=dict(descripcion="descripcion {}".format(i), nombre="competencia {}".format(i)))
		print(r.status_code)
		if (r.status_code == 200):
			print("competencia #{} creada".format(i))
			print("Exitoso!")
			print(r.content.decode("utf-8"))
		else:
			print("Fracaso!")
			print(r.content.decode("utf-8"))


if __name__ == '__main__':
	testCrearCompetencias()


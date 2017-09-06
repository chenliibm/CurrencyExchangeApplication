import urllib.request
import json

def setup_module():
	pass


def testCurrencyRateAPI():
	pass

def testAPI():
	url = "http://localhost:5000/api/test"
	response = urllib.request.urlopen(url)
	assert response.status == 200
	assert json.loads(bytes.decode(response.read()))['result'] == 10 
	response.close()


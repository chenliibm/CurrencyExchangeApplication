import urllib.request
import json

def setup_module():
	pass


def testCurrencyRateAPI():
	assert 3==3

def testAPI():
	url = "http://localhost:5000/api/test"
	response = urllib.request.urlopen(url)
	assert response.status == 200
	assert json.loads(response.read())['result'] == 10 


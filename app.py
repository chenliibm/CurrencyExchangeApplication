from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


email_addresses = []

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/api/currencyrate', methods = ['GET'])
def getCurrencyRate():
    return jsonify({'tasks': tasks})

@app.route('/api/test', methods = ['GET'])
def getTest():
    return jsonify({"result": 10})

	
if __name__ == '__main__':
	app.run(debug=True)
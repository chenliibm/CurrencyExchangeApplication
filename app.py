from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)






@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/setcurrencyrate', methods = ['POST'])
def setCurrencyRate():
    currencyname = request.form['currencyname']
    date = request.form['date']
    return redirect('/')


@app.route('/api/test', methods = ['GET'])
def getTest():
    return jsonify({"result": 10})

	
if __name__ == '__main__':
	app.run(debug=True)
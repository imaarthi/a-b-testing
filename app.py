from flask import Flask, redirect, render_template
from flask import request
import sys
import random
import json
import csv

sys.dont_write_bytecode = True
with open('./test.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	writer.writerow(['numClicksMemphis'])

app = Flask(__name__)
app.config['DEBUG'] = True

# Simple python Flask server

@app.route('/', methods=['GET'])
def root():
	probability = random.uniform(0, 1)
	if probability < 0.5:
		return render_template('A.html')
	else:
		return render_template('B.html')



@app.route('/data', methods=['GET', 'POST'])
def get_data():
	return request.data
	data = json.loads(request.data)
	n_clicks = data.get('numClicksMemphis')
	writer.writerow(n_clicks)
	return "Ok"


if __name__ == '__main__':
    app.run(debug=True)

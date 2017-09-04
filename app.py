from flask import Flask, redirect
from flask import request
import sys
import json
import csv

sys.dont_write_bytecode = True
with open('./test.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	writer.writerow(['numClicksMemphis'])

app = Flask(__name__)
app.config['DEBUG'] = True

# Simple python Flask server

@app.route('/')
def root():
	redirect('main.html')

@app.route('/data')
def get_data():

	data = json.loads(request.data)
	n_clicks = data.get('numClicksMemphis')

	writer.writerow(n_clicks)

from flask import Flask
import sys

sys.dont_write_bytecode = True


app = Flask(__name__)
app.config['DEBUG'] = True

# Simple python Flask server

@app.route('/')
def admin():
	return "OK"

@app.route('/data')
def admin():
	return "OK"
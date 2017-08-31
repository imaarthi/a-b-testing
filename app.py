import os

from flask import Flask
from flask import render_template
from flask.ext.split import split

app = Flask(__name__)
app.register_blueprint(split)


@app.route("/")
def start():
	render_template('hello.html')


if __name__ == "__main__":
	port = 5000
	app.run(host='0.0.0.0', port=port)

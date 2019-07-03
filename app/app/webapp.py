import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>HELLO WORLD</h1>"

def run(host, port, debug=True):
  if debug:
    os.environ['FLASK_ENV'] = "development"
  app.run(host=host, port=port, debug=debug)

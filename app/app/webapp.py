import os

from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/chap6', methods=['GET'])
def chap6():
  return render_template("chap6.html", request=request)

@app.route('/api/sales')
def sales():
  return open('app/static/sales.json').read()


def run(host, port, debug=True):
  if debug:
    os.environ['FLASK_ENV'] = "development"
  app.run(host=host, port=port, debug=debug)

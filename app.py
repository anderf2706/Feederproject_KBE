import math
import time

from flask import Flask, render_template, request, jsonify

from DFAServer3 import run
from DisplayRail import automate
import PathPlanner

app = Flask(__name__, static_url_path='/static/')

"""
@app.route('/process',methods= ['GET', 'POST'])
def process():
  list = request.form['list']
  output = list
  return jsonify({'output': 'Full Name: ' + output})
"""


@app.route('/', methods=['GET', 'POST'])
def render():
    if request.method == 'POST':
        #global data
        #data = [(2,4),(7,10)]
        run()
        time.sleep(1)
        automate()
        #time.sleep(8)
        return render_template('test.html')
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')


if __name__ == '__main__':
    #findPath()
    app.run(debug=True)


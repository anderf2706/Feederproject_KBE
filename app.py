import math
import time

from flask import Flask, render_template, request, jsonify

from DFAServer3 import run
from DisplayRail import automate
import PathPlanner
from Updatepoints import update

app = Flask(__name__, static_url_path='/static/')


@app.route('/', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
        global points
        global obsticles
        global heights
        points = request.form['points']
        obsticles = request.form['obsticles']
        heights = request.form['heights']
        print('mine points er  ' + points)
        print('mine obst er  ' + obsticles)
        results = heights.split(',')
        heights = (list(map(int, results)))
        print(heights)
        points = update(points)
        obsticles = update(obsticles)
        run(points, obsticles, heights)
        time.sleep(1)
        automate()
        # time.sleep(8)
        return render_template('test.html')
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')


if __name__ == '__main__':
    #findPath()
    app.run(debug=True)


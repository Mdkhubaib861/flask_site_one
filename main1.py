from flask import Flask, render_template, request
import math
Myapp = Flask(__name__)

@Myapp.route('/')
def index():
    return render_template('home.html')

@Myapp.route('/result')
def result():
    return render_template('result.html')

@Myapp.route('/calculate')
def calculate():
    return render_template('calculate.html')


Myapp.run(debug=True)
from app import app
from flask import Flask, render_template


@app.route('/')
@app.route('/home')
def index():                             
    return render_template('index.html')

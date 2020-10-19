from app import app
from flask import Flask, render_template

@app.route('/api/')
def inde():
	return render_template("static/index.html")

@app.route('/home')
def index():                             
    return render_template('/home/djo/Youlearn/YouLearn/static/index.html')

from app import app
from flask import Flask, render_template
from app.forms import SignupForm


@app.route('/')
@app.route('/home')
def index():
    form = SignupForm()                         
    return render_template('index.html', title='YouLearn', form=form)

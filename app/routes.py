from app import app
from flask import Flask, render_template, redirect, url_for
from app.forms import SignupForm
from flask_login import login_required, current_user, logout_user


@app.route('/')
@app.route('/home')
def index():
    form = SignupForm()                         
    return render_template('index.html', title='YouLearn', form=form)

@app.route('/profile')
@login_required
def profile():
	profile = {'email':current_user.email,'name':current_user.name, 'lastname':current_user.lastname, 'profession': current_user.profession, 'telephone': current_user.telephone}
	return render_template('profile.html', title='Profile', profile=profile)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
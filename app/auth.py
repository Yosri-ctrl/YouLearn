from app import app,db
from app.models.user import User
from flask import request, abort, render_template, url_for, g, redirect, flash
from app.forms import SignupForm
from flask_login import login_user

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    lastname = request.form.get('lastname')
    telephone = request.form.get('telephone')
    profession = request.form.get('profession')
    if email is None or password is None:
            abort(400) # missing arguments
    if User.query.filter_by(email = email).first() is not None:
            abort(400) # existing user
    user = User(email = email, name = name, lastname = lastname, telephone = telephone, profession = profession)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not user.verify_password(password):
        flash('Please check your login details and try again.')
        return redirect(url_for('index'))
    login_user(user, remember=remember)
    return redirect(url_for('index'))
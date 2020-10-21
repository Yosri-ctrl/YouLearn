from app import app,db
from app.models.user import User
from flask import request, abort, jsonify, url_for, g
from forms import SignupForm

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
    user = User(email = email, name=name, lastname = lastname, telephone = telephone)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index.html'))

@app.route('/signup')
def signup():
	form = SignupForm()
	

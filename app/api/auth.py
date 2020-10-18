from flask import request, abort, jsonify, url_for, g
from app import app,db
from app.models.user import User
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

@app.route('/api/users', methods=['POST'])
def add_user():
    """
    adds new user to database
    @email
    @password
    @name
    @lastname
    @telephone
    returns user.id and location header for get user
    """
    email = request.json.get('email')
    name = request.json.get('name')
    password = request.json.get('password')
    lastname = request.json.get('lastname')
    telephone = request.json.get('telephone')
    if email is None or password is None:
            abort(400) # missing arguments
    if User.query.filter_by(email = email).first() is not None:
            abort(400) # existing user
    user = User(email = email, name=name, lastname = lastname, telephone = telephone)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'id': user.id}), 201,
                {'Location': url_for('get_user', id=user.id, _external=True)})

@app.route('/api/users/<int:id>')
def get_user(id):
    """returns user"""
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'email': user.email, 'name': user.name, 'lastname': user.lastname,'telephone' :user.telephone})

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })


@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(email = email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.name})
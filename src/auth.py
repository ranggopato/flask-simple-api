
from wsgiref.validate import validator
from flask import Blueprint, request, jsonify
from sqlalchemy import Identity, true
import validators
from werkzeug.security import check_password_hash, generate_password_hash
from src.database import User, db
from src.constants.http_status_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token
auth = Blueprint('auth',__name__, url_prefix= "/api/auth"  )

@auth.post('/register-cat')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(password) < 6:
        return jsonify({"error" : "Password too short"}), HTTP_400_BAD_REQUEST
    if len(username) < 3:
        return jsonify({"error" : "Username too short"}), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({"error" : "Username should be alphanumeric, also no space"}), HTTP_400_BAD_REQUEST
    if not validators.email(email) :
        return jsonify({"error": "Email is not valid"}), HTTP_400_BAD_REQUEST
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error":"User is already exist"}), HTTP_409_CONFLICT
    pwd_hash = generate_password_hash(password)
    user = User(username=username, email = email, password = pwd_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message" : "User created",
        "user" : {
            "username" : username,
            "email": email
        }
    }), HTTP_201_CREATED

@auth.post('/login')
def login():
    email = request.json.get('email','')
    password = request.json.get('password','')

    user = User.query.filter_by(email = email).first()

    if user:
        is_pass_correct = check_password_hash(user.password, password)
        if is_pass_correct:
            refresh = create_refresh_token(identity = user.id)
            access = create_access_token(identity=user.id)
            return jsonify({'user': {
                'refresh' : refresh,
                'access' : access,
                'username' : user.username,
                'email': user.email
            }}), HTTP_200_OK
        return jsonify({'error': 'Wrong Credentials'}),HTTP_401_UNAUTHORIZED
            
        
@auth.get('/mycat')
@jwt_required()
def my_cat():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return jsonify ({
        'username': user.username,
        'email' : user.email
    }), HTTP_200_OK

@auth.post('/token/refresh')
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        'access' : access
    }),HTTP_200_OK



@auth.get('/mykucing')
def my_kucing():
    return {"catName" : "Tek Ayu"}
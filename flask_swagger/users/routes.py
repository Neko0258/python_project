from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_swagger.errors import handler
from flask_swagger import bcrypt
from flask_swagger import client

users = Blueprint('users', __name__)

collection = client.collection
user_collection = collection.user_collection

@users.route('/register', methods=['POST'])
def register():
    #get username, email and password from request data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']

    pw_hashed = bcrypt.generate_password_hash(password).decode('utf-8') #hashing password
    #checking username and email in database
    check_user = user_collection.find_one({'username': username})
    check_email = user_collection.find_one({'email': email})

    if not (check_user or check_email) and password:
        user_collection.insert({'username': username, 'password': pw_hashed,'email': email, 'role': role}) #insert to database
        response = jsonify(message='Your account have been create success!') #message success after insert
        response.status_code = 201 #status code
        return response
    else:
        return handler.not_found()
    
#login, check the username and the password

@users.route('/login', methods=['GET', 'POST'])
def login():
    #get username and password from request data
    username = request.args.get("username")
    password = request.args.get("password")
    
    pw = user_collection.find_one({"username": username}, {"password"})
    check_pw = bcrypt.check_password_hash(pw["password"], password) #check hashed password
    check_user = user_collection.find({"username": username})


    if check_user and check_pw:
        access_token = create_access_token(identity=username)
        response = jsonify(message='Login sucesss!', access_token=access_token)
        response.set_cookie(access_token)
        response.status_code = 200
        return response
    else:
        return handler.not_found()

#verify email
@users.route('/verifyemail', methods=['GET'])
def verifyemail():
    email = request.args.get("email") #get email from request
    check_email = user_collection.find_one({"email": email})
    if check_email:
        response = jsonify(message='A verify email has been sent to your email address!')
        response.status_code = 200
        return response
    else:
        return handler.not_found()
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_swagger.config import Config
from pymongo import MongoClient
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

jwt = JWTManager()
bcrypt = Bcrypt()
client = MongoClient(Config.MONGODB_URI)

def create_app(config_class=Config):
    app = Flask(__name__)
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.config.from_object(Config)
    app.config["JWT_SECRET_KEY"] = "sweet_secret_key"
    
    from flask_swagger.main.routes import swag
    from flask_swagger.users.routes import users
    from flask_swagger.products.routes import products
    from flask_swagger.errors.handler import errors
    app.register_blueprint(swag)
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(errors)

    return app

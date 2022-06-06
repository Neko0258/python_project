from flask import Flask
from flask_bcrypt import Bcrypt
from flask_swagger.config import Config
from pymongo import MongoClient
bcrypt = Bcrypt()
client = MongoClient(Config.MONGODB_URI)
"""
if os.environ["app"] == "prod":
    client = MongoClient("mongodb://neko:123@192.168.32.124:27017")
else:
    client = MongoClient("mongodb://neko:123@192.168.32.124:27017")
"""
def create_app(config_class=Config):
    app = Flask(__name__)
    bcrypt.init_app(app)
    app.config.from_object(Config)
    from flask_swagger.main.routes import swag
    from flask_swagger.users.routes import users
    from flask_swagger.products.routes import products
    from flask_swagger.errors.handler import errors
    
    app.register_blueprint(swag)
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(errors)

    return app

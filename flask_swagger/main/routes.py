from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint

swag = Blueprint('swag', __name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app-name': "RESTFUL API PYTHON MONGODB"
    }
)

swag.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
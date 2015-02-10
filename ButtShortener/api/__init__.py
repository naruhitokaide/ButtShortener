from flask import Blueprint
from flask.ext.restful import Api

api = Blueprint('api', __name__)
restv1 = Api(api, prefix="/v1")
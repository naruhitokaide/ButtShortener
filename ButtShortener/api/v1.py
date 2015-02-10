from ButtShortener.api import restv1
from flask.ext.restful import Resource, reqparse

parser = reqparse.RequestParser()


class MainResource(Resource):
    def post(self):
        '''Create a new short URL'''
        args = parser.parse_args()
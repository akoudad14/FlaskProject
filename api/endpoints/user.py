from flask_restplus import Resource
from api.api import api
from Controller.UserController import UserController
from flask import jsonify

user_ns = api.namespace('users')


@user_ns.route('/')
class Users(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = UserController()

    def get(self):
        """Function to get all the users in the database"""
        users = self._controller.get_all()
        return jsonify(users)

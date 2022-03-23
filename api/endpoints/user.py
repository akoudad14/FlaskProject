
from flask import Response
from flask_restplus import Resource, fields
from flask import request, jsonify
from werkzeug.security import generate_password_hash
import uuid

from api.api import api
from Controller.UserController import UserController

user_ns = api.namespace('users')

user_model = user_ns.model('User insert', {
    'name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})


@user_ns.route('/')
class User(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = UserController()

    def get(self) -> Response:
        """Retrieves users from the database."""
        users = self._controller.get_users()
        return jsonify(users)

    @user_ns.doc(body=user_model)
    def post(self):
        controller = UserController()
        data = request.json
        hashed_password = generate_password_hash(data['password'],
                                                 method='sha256')
        controller.add_user(public_id=str(uuid.uuid4()), name=data['name'],
                            password=hashed_password, email=data['email'])
        return jsonify({'message': 'registered successfully'})


@user_ns.route('/<int:id>')
class Users(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = UserController()

    def get(self, id: int) -> Response:
        """Retrieves one user from the database"""
        user = self._controller.get_user_by_filter(id)
        return jsonify(user)

    @user_ns.doc(body=user_model)
    def put(self, id: int) -> Response:
        self._controller.update_user(id, request.json)
        return Response('User updated', 204)

    def delete(self, id: int) -> Response:
        self._controller.delete_user(id)
        return Response('User deleted', 204)

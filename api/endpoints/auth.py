from flask_restplus import Resource, fields
from flask import request, jsonify, make_response
from werkzeug.security import check_password_hash
import jwt
import datetime
from functools import wraps

from api.api import api
from Controller.UserController import UserController

auth_ns = api.namespace('auth', validate=True)

login_user_model = auth_ns.model('User login', {
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'HTTP_AUTHORIZATION' in request.headers.environ:
            token = request.headers.environ['HTTP_AUTHORIZATION']
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, 'SECRET_KEY')
        except:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)
    return decorator


@auth_ns.route("/login")
class LoginUser(Resource):

    @auth_ns.doc(body=login_user_model)
    def post(self):
        controller = UserController()
        data = request.json
        user = controller.get_user_by_filter(email=data['email'])
        if user and check_password_hash(user.password, data['password']):
            token = jwt.encode({'public_id': user.public_id,
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(
                                    minutes=30)}, 'SECRET_KEY')
            return jsonify({'token': token.decode('UTF-8')})
        return make_response('could not verify', 401, {
            'WWW.Authentication': 'Basic realm: "login required"'
        })


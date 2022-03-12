
from flask import jsonify, Response
from flask_restplus import Resource

from api.api import api
from Controller.CharacterController import CharacterController

character_ns = api.namespace('characters')


@character_ns.route('/')
class Characters(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = CharacterController()

    def get(self) -> Response:
        """Retrieves all characters from the database"""
        characters = self._controller.get_all()
        return jsonify(characters)


from flask import jsonify, Response
from flask_restplus import Resource

from api.api import api
from api.endpoints.auth import token_required
from Controller.RessourceController import RessourceController

episode_ns = api.namespace('episodes')


@episode_ns.route('/')
class Episode(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = RessourceController()

    @token_required
    def get(self) -> Response:
        """Retrieves all episodes from the database"""
        episodes = self._controller.get_episodes()
        return jsonify(episodes)

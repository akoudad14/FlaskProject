
from flask import jsonify, Response
from flask_restplus import Resource

from api.api import api
from Controller.RessourceController import RessourceController

episode_ns = api.namespace('episodes')


@episode_ns.route('/')
class Episodes(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = RessourceController()

    def get(self) -> Response:
        """Retrieves all episodes from the database"""
        episodes = self._controller.get_episodes()
        return jsonify(episodes)

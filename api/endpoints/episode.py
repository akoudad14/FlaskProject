
from flask import jsonify, Response
from flask_restplus import Resource

from api.api import api
from Controller.EpisodeController import EpisodeController

episode_ns = api.namespace('episodes')


@episode_ns.route('/')
class Episodes(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = EpisodeController()

    def get(self) -> Response:
        """Retrieves all episodes from the database"""
        episodes = self._controller.get_all()
        return jsonify(episodes)

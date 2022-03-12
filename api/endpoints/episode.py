from flask_restplus import Resource
from api.api import api
from Controller.EpisodeController import EpisodeController
from flask import jsonify

episode_ns = api.namespace('episode')


@episode_ns.route('/')
class Users(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = EpisodeController()

    def get(self):
        episodes = self._controller.get_all()
        return jsonify(episodes)

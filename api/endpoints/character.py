
from flask import jsonify, Response, request
from flask_restplus import Resource

from api.api import api
from Controller.ApiController import ApiController

character_ns = api.namespace('characters')

parser = api.parser()
parser.add_argument('start', type=int)
parser.add_argument('limit', type=int)


@character_ns.route('/')
class Characters(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = ApiController()

    @api.expect(parser)
    def get(self) -> Response:
        """Retrieves characters from the database."""
        start = int(request.args.get('start', 0))
        try:
            limit = int(request.args.get('limit'))
        except TypeError:
            limit = None
        characters = self._controller.get_characters(start, limit)
        return jsonify(characters)

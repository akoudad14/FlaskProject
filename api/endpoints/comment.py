
from flask import jsonify, Response, request
from flask_restplus import Resource, fields

from api.api import api
from Controller.ApiController import ApiController

comment_ns = api.namespace('comments')

insert_comment_model = comment_ns.model('Comment insert', {
    'comment': fields.String(
        required=True,
        description='The comment to save.'),
    'character_id': fields.Integer(
        description=r"Character id to associate the comment with."),
    'episode_id': fields.Integer(
        description=r"Episode id to associate the comment with.")
})


update_comment_model = comment_ns.model('Comment update', {
    'comment': fields.String(
        required=True,
        description='The comment to save.')
})

parser = api.parser()
parser.add_argument('start', type=int)
parser.add_argument('limit', type=int)


@comment_ns.route('/')
class Comments(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = ApiController()

    @api.expect(parser)
    def get(self) -> Response:
        """Retrieves comments from the database."""
        start = int(request.args.get('start', 0))
        try:
            limit = int(request.args.get('limit'))
        except TypeError:
            limit = None
        comments = self._controller.get_comments(start, limit)
        return jsonify(comments)

    @comment_ns.doc(body=insert_comment_model)
    def post(self) -> Response:
        """Creates comment in the database."""
        self._controller.add_comment(request.json)
        return Response('Comment created', 201)


@comment_ns.route('/<int:id>')
class Comments(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = ApiController()

    def get(self, id: int) -> Response:
        """Retrieves one comment from the database"""
        comment = self._controller.get_one_comment(id)
        return jsonify(comment)

    @comment_ns.doc(body=update_comment_model)
    def put(self, id: int) -> Response:
        self._controller.update_comment(id, request.json)
        return Response('Comment updated', 204)

    def delete(self, id: int) -> Response:
        self._controller.delete_comment(id)
        return Response('Comment deleted', 204)

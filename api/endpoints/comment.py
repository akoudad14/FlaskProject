
from flask import jsonify, Response, request
from flask_restplus import Resource, fields

from api.api import api
from Controller.ApiController import ApiController

comment_ns = api.namespace('comments')

comment_model = comment_ns.model('Comment', {
    'comment': fields.String(
        required=True,
        description='The comment to save.'),
    'character_id': fields.Integer(
        description=r"Character id to associate the comment with."),
    'episode_id': fields.Integer(
        description=r"Episode id to associate the comment with."),
    'character_episode_id': fields.Integer(
        description=r"The id of a character from an episode to "
                    r"associate the comment with."),
})


@comment_ns.route('/')
class Comments(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = ApiController()

    def get(self) -> Response:
        """Retrieves all comments from the database"""
        comments = self._controller.get_all_comments()
        return jsonify(comments)

    @comment_ns.doc(body=comment_model)
    def post(self) -> Response:
        self._controller.add_comment(request.json)
        return Response('Comment created', 201)


@comment_ns.route('/<int:id>')
class Comments(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._controller = ApiController()

    def get(self, id: int) -> Response:
        """Retrieves all comments from the database"""
        comments = self._controller.get_all_comments()
        return jsonify(comments)

    def put(self, id: int) -> Response:
        pass

    def delete(self, id: int) -> Response:
        pass

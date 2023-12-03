from flask import Blueprint, jsonify, request
from dtos.responses import *
from services import CommentService
from dtos import CommentDto
import json

comment_blueprint = Blueprint('comment', __name__)


@comment_blueprint.route('/comment', methods=['POST'])
def postComment() -> (Response, int):
    req_data: dict = request.get_json()
    commentService = CommentService()
    commentDto = CommentDto.fromJson(req_data)
    response: json = commentService.postComment(commentDto)
    json_res = json.dumps(response, default=lambda o: o.__dict__)
    return json_res, response.get('status')


@comment_blueprint.route('/comment/p/<int:postId>', methods=['GET'])
def getPostComments(postId) -> (Response, int):
    commentService = CommentService()
    response: json = commentService.getPostComments(postId)
    json_res = json.dumps(response, default=lambda o: o.__dict__)
    return json_res, response.get('status')


@comment_blueprint.route('/comment/<int:commentId>', methods=['GET'])
def getComment(commentId) -> (Response, int):
    commentService = CommentService()
    response: json = commentService.getComment(commentId)
    json_res = json.dumps(response, default=lambda o: o.__dict__)
    return json_res, response.get('status')


@comment_blueprint.route('/comment/<int:commentId>', methods=['DELETE'])
def deleteComment(commentId) -> (Response, int):
    commentService = CommentService()
    response: json = commentService.deleteComment(commentId)
    json_res = json.dumps(response, default=lambda o: o.__dict__)
    return json_res, response.get('status')

from flask import Blueprint, jsonify, request

from services import PostService
from dtos import PostDto
from dtos.responses import Response

post_blueprint = Blueprint('post', __name__)


@post_blueprint.route('/post/id/<int:id>', methods=['GET'])
def getSinglePost(id: int) -> (Response, int):
    ps: PostService = PostService()
    res: dict = ps.getPost(id)
    return jsonify(res), res.status


@post_blueprint.route('/post/id/<int:id>', methods=['DELETE'])
def deleteSinglePost(id: int) -> (Response, int):
    ps: PostService = PostService()
    res: dict = ps.deletePost(id)
    return jsonify(res), res.status


@post_blueprint.route('/post/u/<string:username>', methods=['GET'])
def getUserPosts(username: str) -> (Response, int):
    ps: PostService = PostService()
    res: dict = ps.getUserPosts(username)
    return jsonify(res), res.status


@post_blueprint.route('/post/g/<int:groupId>', methods=['GET'])
def getGroupPosts(groupId: int) -> (Response, int):
    ps: PostService = PostService()
    res: dict = ps.getGroupPosts(groupId)
    return jsonify(res), res.status


@post_blueprint.route('/post', methods=['POST'])
def createPost() -> (Response, int):
    data: dict = request.get_json()
    post: PostDto = PostDto.fromJson(data)
    ps: PostService = PostService()
    res: dict = ps.createPost(post)
    return jsonify(res), res.status

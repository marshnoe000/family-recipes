from flask import Blueprint, jsonify, request

from services import PostService
from dtos import PostDto

post_blueprint = Blueprint('post', __name__)


# TODO error handling
@post_blueprint.route('/post/id/<int:id>', methods=['GET'])
def getSinglePost(id: int):
    ps: PostService = PostService(False)
    res: dict = ps.getPost(id)
    return jsonify(res), res["status"]


# Should this be combined with the route above?
# Maybe a single handlePostById()?
# I guess it doesn't really matter whether the router
# handles the method differentiation vs our code
@post_blueprint.route('/post/id/<int:id>', methods=['DELETE'])
def deleteSinglePost(id: int):
    ps: PostService = PostService(False)
    res: dict = ps.deletePost(id)
    return jsonify(res), res["status"]


@post_blueprint.route('/post/u/<string:username>', methods=['GET'])
def getUserPosts(username: str):
    ps: PostService = PostService(False)
    res: dict = ps.getUserPosts(username)
    return jsonify(res), res["status"]


@post_blueprint.route('/post/g/<int:groupId>', methods=['GET'])
def getGroupPosts(groupId: int):
    ps: PostService = PostService(False)
    res: dict = ps.getGroupPosts(groupId)
    return jsonify(res), res["status"]


@post_blueprint.route('/post', methods=['POST'])
def createPost():
    data: dict = request.get_json()
    post: PostDto = PostDto.fromJson(data)
    ps: PostService = PostService(False)
    res: dict = ps.makePost(post)
    return jsonify(res), res["status"]

from flask import Blueprint, jsonify, request

from services import PostService
from dtos import PostDto
from dtos.responses import Response
from controllers import boolFromQuery

post_blueprint = Blueprint('post', __name__)


@post_blueprint.route('/post/<int:id>', methods=['GET'])
def getSinglePost(id: int) -> (Response, int):
    embedRecipe = boolFromQuery(request.args.get('embed'), default=True)
    ps: PostService = PostService()
    res: dict = ps.getPost(id, embedRecipe)
    return jsonify(res), res.status


@post_blueprint.route('/post/<int:id>', methods=['DELETE'])
def deleteSinglePost(id: int) -> (Response, int):
    ps: PostService = PostService()
    res: dict = ps.deletePost(id)
    return jsonify(res), res.status


@post_blueprint.route('/post/u/<string:username>', methods=['GET'])
def getUserPosts(username: str) -> (Response, int):
    embedRecipe = boolFromQuery(request.args.get('embed'), default=True)
    ps: PostService = PostService()
    res: dict = ps.getUserPosts(username, embedRecipe)
    return jsonify(res), res.status


@post_blueprint.route('/post/g/<int:groupId>', methods=['GET'])
def getGroupPosts(groupId: int) -> (Response, int):
    embedRecipe = boolFromQuery(request.args.get('embed'), default=True)
    ps: PostService = PostService()
    res: dict = ps.getGroupPosts(groupId, embedRecipe)
    return jsonify(res), res.status


@post_blueprint.route('/post', methods=['POST'])
def createPost() -> (Response, int):
    data: dict = request.get_json()
    post: PostDto = PostDto.fromJson(data)
    ps: PostService = PostService()
    res: dict = ps.makePost(post)
    return jsonify(res), res.status

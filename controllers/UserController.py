import string

from flask import Blueprint, jsonify, request
from services.UserService import UserService
from dtos.UserDto import UserDto
from dtos.responses import Response

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user/<string:username>', methods=['GET'])
def getUser(username: string) -> (Response, int):
    us: UserService = UserService()
    res: dict = us.getUser(username)
    return jsonify(res), res["status"]


@user_blueprint.route('/user/<string:username>', methods=['DELETE'])
def deleteUser(username: string) -> (Response, int):
    us: UserService = UserService()
    res: dict = us.deleteUser(username)
    return jsonify(res), res["status"]


@user_blueprint.route('/user/register', methods=['POST'])
def register() -> (Response, int):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    userDto = UserDto(username, password, email, name)

    userService = UserService()

    userService.register(userDto)
    return jsonify({"username": username}), 201

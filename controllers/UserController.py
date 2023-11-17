import string

from flask import Blueprint, jsonify, request
from services.UserService import UserService
from dtos.UserDto import UserDto
from dtos.responses import Response

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user/<string:username>', methods=['GET'])
def getUser(username: string) -> (Response, int):
    userService: UserService = UserService()

    response: dict = userService.getUser(username)
    return jsonify(response), response["status"]


@user_blueprint.route('/user/<string:username>', methods=['DELETE'])
def deleteUser(username: string) -> (Response, int):
    userService: UserService = UserService()

    response: dict = userService.deleteUser(username)
    return jsonify(response), response["status"]


@user_blueprint.route('/user/register', methods=['POST'])
def register() -> (Response, int):
    data: dict = request.get_json()
    userDto: UserDto = UserDto.fromJson(data)
    userService: UserService = UserService()

    response: dict = userService.register(userDto)
    return jsonify(response), response["status"]


@user_blueprint.route('/user/login', methods=['POST'])
def login() -> (Response, int):
    data: dict = request.get_json()
    userDto: UserDto = UserDto.fromJson(data)
    userService: UserService = UserService()

    response: dict = userService.login(userDto)
    return jsonify(response), response["status"]

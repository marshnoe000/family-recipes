from flask import Blueprint, jsonify, request
from services.UserService import UserService
from dtos.UserDto import UserDto
from dtos.responses import Response

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user', methods=['GET'])
def getUser():
    data = {'message': 'This is the response from the user endpoint'}
    return jsonify(data)


@user_blueprint.route('/user/register', methods=['POST'])
def register() -> (Response, int):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    userDto = UserDto(username, password, email, name)
    isProd = True if data.get('isProd') == "True" else False

    userService = UserService(isProd)

    userService.register(userDto)
    return jsonify({"status": 201}), 201

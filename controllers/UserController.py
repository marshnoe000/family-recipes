from flask import Blueprint, jsonify, request, make_response
from services.UserService import UserService

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user', methods=['GET'])
def getUser():
    data = {'message': 'This is the response from the user endpoint'}
    return jsonify(data)


@user_blueprint.route('/user/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    isProd = True if data.get('isProd') == "True" else False

    userService = UserService(isProd)

    successful = userService.register(username, password, email, name)
    status = 201 if successful else 400
    response = jsonify({'status': status})
    return response, status

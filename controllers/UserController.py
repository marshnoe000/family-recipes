from flask import Blueprint, jsonify

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/user', methods=['GET'])
def getUser():
    data = {'message': 'This is the response from the user endpoint'}
    return jsonify(data)

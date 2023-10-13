from flask import Blueprint, jsonify

post_blueprint = Blueprint('post', __name__)


@post_blueprint.route('/post', methods=['GET'])
def getPost():
    data = {'message': 'This is the response from the post endpoint'}
    return jsonify(data)

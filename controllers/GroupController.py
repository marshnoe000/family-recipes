from flask import Blueprint, jsonify

group_blueprint = Blueprint('group', __name__)


@group_blueprint.route('/group', methods=['GET'])
def getGroup():
    data = {'message': 'This is the response from the group endpoint'}
    return jsonify(data)

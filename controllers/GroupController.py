from flask import Blueprint, jsonify, request

from services import GroupService
from dtos import GroupDto
from dtos.responses import Response
from dtos.errors import BadRequestError

group_blueprint = Blueprint('group', __name__)


@group_blueprint.route('/group', methods=['POST'])
def makeGroup() -> (Response, int):
    data: dict = request.get_json()
    group: GroupDto = GroupDto.fromJson(data)
    gs: GroupService = GroupService(False)
    res: dict = gs.makeGroup(group)
    return jsonify(res), res["status"]


@group_blueprint.route('/group/<int:groupId>/users', methods=['GET'])
def getGroupMembers(groupId: int) -> (Response, int):
    return 'as\n'


@group_blueprint.route('/group/<int:groupId>/users', methods=['POST', 'DELETE'])
def groupMembersHandler(groupId) -> (Response, int):
    data: dict = request.get_json()
    username: str = data.get('username')
    print(username)
    if username is None or len(username) < 1:
        raise BadRequestError(f"Expected username, got '{username}'")
    gs: GroupService = GroupService(False)

    res: dict = None
    match request.method:
        case 'POST':
            res = gs.addUserToGroup(groupId, username)
        case 'DELETE':
            res = gs.removeUserFromGroup(groupId, username)

    return jsonify(res), res.status

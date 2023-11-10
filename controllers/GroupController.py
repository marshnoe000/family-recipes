from flask import Blueprint, jsonify, request

from services import GroupService
from dtos import GroupDto
from dtos.responses import Response, ErrorResponse

group_blueprint = Blueprint('group', __name__)


@group_blueprint.route('/group', methods=['POST'])
def makeGroup() -> (Response, int):
    data: dict = request.get_json()
    group: GroupDto = GroupDto.fromJson(data)
    gs: GroupService = GroupService(False)
    try:
        res: dict = gs.makeGroup(group)
    except Exception as e:
        res: dict = ErrorResponse(e)
    return jsonify(res), res["status"]


@group_blueprint.route('/group/add', methods=['POST'])
def addUserToGroup() -> (Response, int):
    data: dict = request.get_json()
    groupId: int = data.get('groupId')
    username: str = data.get('username')
    gs: GroupService = GroupService(False)
    res: dict = gs.addUserToGroup(groupId, username)
    return jsonify(res), res["status"]

from flask import Blueprint, jsonify, request

from services import GroupService
from dtos import GroupDto
from dtos.responses import Response
from controllers import boolFromQuery

group_blueprint = Blueprint('group', __name__)


@group_blueprint.route('/group/<int:groupId>', methods=['GET'])
def getGroup(groupId: int) -> (Response, int):
    gs: GroupService = GroupService()
    getUsers = boolFromQuery(request.args.get("members"))
    res: dict = gs.getGroup(groupId, getUsers)
    return jsonify(res), res.status


@group_blueprint.route('/group', methods=['POST'])
def makeGroup() -> (Response, int):
    data: dict = request.get_json()
    group: GroupDto = GroupDto.fromJson(data)
    gs: GroupService = GroupService()
    res: dict = gs.makeGroup(group)
    return jsonify(res), res.status


@group_blueprint.route('/group/<int:groupId>/users', methods=['GET'])
def getGroupMembers(groupId: int) -> (Response, int):
    gs: GroupService = GroupService()
    res: dict = gs.getGroupMembers(groupId)
    return jsonify(res), res.status


@group_blueprint.route('/group/<int:groupId>/users', methods=['POST'])
def addUserToGroup(groupId: int) -> (Response, int):
    data: dict = request.get_json()
    username: str = data.get('username')
    gs: GroupService = GroupService()
    res: dict = gs.addUserToGroup(groupId, username)
    return jsonify(res), res.status


@group_blueprint.route('/group/<int:groupId>/users', methods=['DELETE'])
def removeUserFromGroup(groupId: int) -> (Response, int):
    username: str = request.args.get('username')
    gs: GroupService = GroupService()
    res = gs.removeUserFromGroup(groupId, username)
    return jsonify(res), res.status

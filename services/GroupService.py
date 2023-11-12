from flask import current_app as app

from repositories import GroupRepository
from dtos import GroupDto
from dtos.responses import DataResponse, CreateResponse, DeleteResponse
from dtos.errors import BadRequestError, NotFoundError


class GroupService:
    def __init__(self):
        self.groupRepo = GroupRepository()

    def getGroup(self, groupId: int, getUsers: bool) -> DataResponse:
        group = self.groupRepo.getGroupById(groupId)
        if group is None:
            raise NotFoundError()
        if getUsers:
            users = self.groupRepo.getGroupMembers(groupId)
            group.members = users

        res = DataResponse(200, group)

        return res

    def makeGroup(self, group: GroupDto) -> CreateResponse:
        if group.name is None or len(group.name) == 0:
            raise BadRequestError("Need group.name to create group")

        app.logger.debug(f"making group: {group}")
        insertedId = self.groupRepo.insertGroup(group)
        res = CreateResponse(201, insertedId)

        return res

    def addUserToGroup(self, groupId: int, username: str) -> CreateResponse:
        if username is None or len(username) < 1:
            raise BadRequestError(f"Invalid username: {username}")

        app.logger.debug(f"adding {username} to group {groupId}")
        self.groupRepo.addUserToGroup(groupId, username)
        res = CreateResponse(201)

        return res

    def removeUserFromGroup(self, groupId: int, username: str) -> DeleteResponse:
        if username is None or len(username) < 1:
            raise BadRequestError(f"Invalid username: {username}")

        app.logger.debug(f"removing {username} from group {groupId}")
        rowsAffected = self.groupRepo.removeUserFromGroup(groupId, username)
        res = DeleteResponse(200, rowsAffected)

        return res

    def getGroupMembers(self, groupId: int) -> DataResponse:
        users = self.groupRepo.getGroupMembers(groupId)
        res = DataResponse(200, users)

        return res

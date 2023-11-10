from flask import current_app as app

from repositories import GroupRepository
from dtos import GroupDto
from dtos.responses import DataResponse, CreateResponse, DeleteResponse
from dtos.errors import BadRequestError


class GroupService:
    def __init__(self, isProd=False):
        self.groupRepo = GroupRepository(isProd)
        pass

    # TODO fix this
    def makeGroup(self, group: GroupDto) -> CreateResponse:
        if group["name"] is None or len(group["name"]) == 0:
            raise BadRequestError("Expected group name")

        app.logger.debug(f"making group: {group}")
        insertedId = self.groupRepo.insertGroup(group)
        res = CreateResponse(201, insertedId)

        return res

    def addUserToGroup(self, groupId: int, username: str) -> CreateResponse:
        app.logger.debug(f"adding {username} to group {groupId}")
        self.groupRepo.addUserToGroup(groupId, username)
        res = DataResponse(201, None)

        return res

    def removeUserFromGroup(self, groupId: int, username: str) -> DeleteResponse:
        app.logger.debug(f"removing {username} from group {groupId}")
        rowsAffected = self.groupRepo.removeUserFromGroup(groupId, username)
        res = DeleteResponse(200, rowsAffected)

        return res

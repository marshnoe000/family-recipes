from flask import current_app as app

from repositories import GroupRepository
from dtos import GroupDto
from dtos.responses import DataResponse
from dtos.errors import BadRequestError


class GroupService:
    def __init__(self, isProd=False):
        self.groupRepo = GroupRepository(isProd)
        pass

    def makeGroup(self, group: GroupDto) -> DataResponse:
        if group["name"] is None or len(group["name"]) == 0:
            raise BadRequestError("Expected group name")

        app.logger.info(f"making group: {group}")
        insertedId = self.groupRepo.insertGroup(group)
        res = DataResponse(201, {"id": insertedId})

        return res

    def addUserToGroup(self, groupId: int, username: str):
        if groupId < 0 or groupId is None:
            raise BadRequestError(f"Expected positive integer for group.groupId, got '{groupId}'")

        if len(username) < 1 or username is None:
            raise BadRequestError(f"Expected username, got '{username}'")

        app.logger.info(f"adding {username} to group {groupId}")
        self.groupRepo.addUserToGroup(groupId, username)
        res = DataResponse(201, None)

        return res

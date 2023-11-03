from flask import current_app as app

from repositories import GroupRepository
from dtos import GroupDto
from dtos.responses import DataResponse
from dtos.errors import BadRequestError


def validateCreateGroup(group: GroupDto):
    if group["name"] is None or len(group["name"]) == 0:
        raise BadRequestError("Expected group name")


class GroupService:
    def __init__(self, isProd=False):
        self.groupRepo = GroupRepository(isProd)
        pass

    def makeGroup(self, group: GroupDto) -> DataResponse:
        app.logger.info(f"making group: {group}")
        validateCreateGroup(group)
        insertedId = self.groupRepo.insertGroup(group)
        res = DataResponse(201, {"id": insertedId})

        return res

    def addUserToGroup(self, groupId: int, username: str):
        app.logger.info(f"adding {username} to group {groupId}")
        self.groupRepo.addUserToGroup(groupId, username)
        # TODO seems strange
        res = DataResponse(201, None)

        return res

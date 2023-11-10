from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import GroupDto


class GroupRepository(BaseRepository):
    INSERT_GROUP = "insert into group_table (name, description, created_at) values (?, ?, datetime())"
    INSERT_USER_GROUP = "insert into user_group (group_id, username) values (?, ?)"
    DELETE_USER_GROUP = "delete from user_group where user_group.groupId = ? and user_group.username = ?"

    def __init__(self, isProd: bool):
        super().__init__(isProd)

    def insertGroup(self, group: GroupDto) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.INSERT_GROUP,
            [group["name"], group["description"]]
        )

        return rs.last_insert_rowid

    def addUserToGroup(self, groupId: int, username: str) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.INSERT_USER_GROUP,
            [groupId, username]
        )

        # HACK not sure what this is returning
        return rs.last_insert_rowid

    def removeUserFromGroup(self, groupId: int, username: str) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.DELETE_USER_GROUP,
            [groupId, username]
        )

        return rs.rows_affected

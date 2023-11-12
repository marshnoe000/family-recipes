from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import GroupDto


class GroupRepository(BaseRepository):
    INSERT_GROUP = "insert into group_table (name, description, created_at) values (?, ?, datetime())"
    INSERT_USER_GROUP = "insert into user_group (group_id, username) values (?, ?)"
    DELETE_USER_GROUP = "delete from user_group where user_group.group_id = ? and user_group.username = ?"
    SELECT_GROUP_USERS = "select user_group.username from user_group where user_group.group_id = ?"
    SELECT_GROUP_BY_ID = "select * from group_table where group_table.id = ?"

    def __init__(self):
        super().__init__()

    def getGroupById(self, groupId: int) -> GroupDto:
        rs: ResultSet = self.execute(
            GroupRepository.SELECT_GROUP_BY_ID,
            [groupId]
        )
        group = GroupDto.fromResultSet(rs)

        return group

    def insertGroup(self, group: GroupDto) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.INSERT_GROUP,
            [group.name, group.description]
        )

        return rs.last_insert_rowid

    def addUserToGroup(self, groupId: int, username: str) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.INSERT_USER_GROUP,
            [groupId, username]
        )

        return rs.last_insert_rowid

    def removeUserFromGroup(self, groupId: int, username: str) -> int:
        rs: ResultSet = self.execute(
            GroupRepository.DELETE_USER_GROUP,
            [groupId, username]
        )

        return rs.rows_affected

    def getGroupMembers(self, groupId: int) -> list[str]:
        rs: ResultSet = self.execute(
            GroupRepository.SELECT_GROUP_USERS,
            [groupId]
        )
        usernames = [row[0] for row in rs]

        return usernames

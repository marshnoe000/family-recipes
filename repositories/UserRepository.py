import string

from libsql_client import ResultSet

from dtos import UserDto
from repositories.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    INSERT_USER_STATEMENT = "INSERT INTO user (username, password_hash, password_salt, email, name) VALUES (?, ?, ?, ?, ?)"
    SELECT_USER_BY_USERNAME = "SELECT * FROM user where user.username = ?"
    DELETE_BY_USERNAME = "DELETE FROM user WHERE user.username = ?"


    def __init__(self):
        super().__init__()

    def registerUser(self, user: UserDto):
        self.execute(
            UserRepository.INSERT_USER_STATEMENT,
            [user.username, user.password,
             user.passwordSalt, user.email,
             user.name])

    def getUserByUsername(self, username):
        rs: ResultSet = self.execute(
            UserRepository.SELECT_USER_BY_USERNAME, [username])

        user = UserDto.fromResultSet(rs)
        return user

    def deleteUserByUsername(self, username: string):
        rs: ResultSet = self.execute(
            UserRepository.DELETE_BY_USERNAME, [username])

        return rs.rows_affected

    def login(self, userDto):
        pass

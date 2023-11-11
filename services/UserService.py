import string
from flask import current_app as app

from dtos import UserDto
from dtos.errors import BadRequestError
from repositories.UserRepository import UserRepository
from dtos.responses import DataResponse, DeleteResponse, CreateResponse


def validateNewUser(user: UserDto):
    badVal = None
    if user["username"] is None or len(user["username"]) == 0:
        badVal = "username"

    if user["password"] is None:
        badVal = "password"

    if user["email"] is None:
        badVal = "email"

    if user["name"] is None:
        badVal = "name"

    if badVal is not None:
        raise BadRequestError(f"Need user.{badVal} to create user")


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def getUser(self, username: string) -> DataResponse:
        user = self.userRepository.getUserByUsername(username)
        status = 404 if user is None else 200
        res = DataResponse(status, user)

        return res

    def deleteUser(self, username: string) -> DeleteResponse:
        usersDeleted = self.userRepository.deleteUserByUsername(username)
        status = 404 if usersDeleted is 0 else 204
        res = DeleteResponse(status, usersDeleted)

        return res

    def register(self, user: UserDto) -> CreateResponse:
        # hash and salt the password here if desired
        validateNewUser(user)
        app.logger.info(f"creating {user}...")
        salt = "salt"
        user["passwordSalt"] = salt
        self.userRepository.registerUser(user)
        res = CreateResponse(201, user["username"])

        return res

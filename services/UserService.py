import hashlib
import hmac
from uuid import uuid4
from flask import current_app as app

from dtos import UserDto
from dtos.errors import BadRequestError, InvalidLoginError
from repositories.UserRepository import UserRepository
from dtos.responses import DataResponse, DeleteResponse, CreateResponse


def validateNewUser(user: UserDto, password: str):
    badVal = None
    if user.username is None or len(user.username) == 0:
        badVal = "username"

    if user.email is None:
        badVal = "email"

    if user.name is None:
        badVal = "name"

    if password is None:
        badVal = "password"

    if badVal is not None:
        raise BadRequestError(f"Need user.{badVal} to create user")


def hashPassword(password, salt) -> str:
    for _ in range(4):
        password += salt
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
    return password


def checkPasswordHash(password: str, targetHash: str, salt: str) -> bool:
    hash = hashPassword(password, salt)
    return hmac.compare_digest(hash, targetHash)


def sanitizeUserRes(user: UserDto) -> UserDto:
    if user is not None:
        del user["passwordHash"]
        del user["passwordSalt"]
    return user


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()

    def getUser(self, username: str) -> DataResponse:
        user = self.userRepository.getUserByUsername(username)
        status = 404 if user is None else 200

        user = sanitizeUserRes(user)
        res = DataResponse(status, user)

        return res

    def deleteUser(self, username: str) -> DeleteResponse:
        usersDeleted = self.userRepository.deleteUserByUsername(username)
        status = 404 if usersDeleted == 0 else 204
        res = DeleteResponse(status, usersDeleted)

        return res

    def register(self, user: UserDto, password: str) -> CreateResponse:
        validateNewUser(user, password)

        app.logger.debug(f"creating {user}...")
        user.passwordSalt = uuid4().hex
        user.passwordHash = hashPassword(password, user.passwordSalt)

        self.userRepository.registerUser(user)
        res = CreateResponse(201, user.username)

        return res

    def login(self, req_username: str, req_password: str) -> DataResponse:
        user = self.userRepository.getUserByUsername(req_username)
        if user is None or req_password is None:
            raise InvalidLoginError()

        if not checkPasswordHash(req_password, user.passwordHash, user.passwordSalt):
            raise InvalidLoginError()

        user = sanitizeUserRes(user)
        res = DataResponse(200, user)

        return res

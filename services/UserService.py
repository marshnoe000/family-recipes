from repositories.UserRepository import UserRepository


class UserService:
    def __init__(self, isProd):
        self.userRepository = UserRepository(isProd)

    def register(self, userDto):
        # hash and salt the password here if desired
        salt = "salt"
        userDto.passwordSalt = salt
        return self.userRepository.registerUser(userDto)

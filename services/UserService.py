from repositories.UserRepository import UserRepository

class UserService:
    def __init__(self, isProd):
        self.userRepository = UserRepository(isProd)

    def register(self, username, password, email, name):
        # hash and salt the password here if desired
        salt = "salt"
        return self.userRepository.registerUser(username, password, salt, email, name)

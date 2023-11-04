from repositories.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    INSERT_USER_STATEMENT = "INSERT INTO user (username, password_hash, password_salt, email, name) VALUES (?, ?, ?, ?, ?)"

    def __init__(self, isProd):
        super().__init__(isProd)

    def registerUser(self, userDto):
        self.execute(
            UserRepository.INSERT_USER_STATEMENT,
            [userDto.username, userDto.password,
             userDto.passwordSalt, userDto.email,
             userDto.name])

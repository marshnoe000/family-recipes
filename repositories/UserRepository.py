from repositories.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    INSERT_USER_STATEMENT = "INSERT INTO user (username, password_hash, password_salt, email, name) VALUES (?, ?, ?, ?, ?)"

    def __init__(self, isProd):
        super().__init__(isProd)

    def registerUser(self, username, password, salt, email, name):
        try:
            self.client.execute(UserRepository.INSERT_USER_STATEMENT, [username, password, salt, email, name])
            return True
        except Exception as e:
            print(e.add_note("Register user failed to insert into table"))
            return False

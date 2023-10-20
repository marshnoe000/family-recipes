class UserDto:
    def __init__(self, username, password, email, name, passwordSalt=""):
        self.username = username
        self.password = password
        self.passwordSalt = passwordSalt
        self.email = email
        self.name = name

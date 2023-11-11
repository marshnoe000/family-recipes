from libsql_client import ResultSet


class UserDto(dict):
    def __init__(self, username, password, email, name, passwordSalt=""):
        super().__init__(
            username=username,
            password=password,
            passwordSalt=passwordSalt,
            email=email,
            name=name,
        )

    def fromJson(json: dict):
        return UserDto(
            json.get('username'),
            json.get('password'),
            json.get('passwordSalt'),
            json.get('email'),
            json.get('name')
        )

    def fromResultSet(rs: ResultSet, forceArray=False):
        if len(rs) == 0:
            return None

        if len(rs) == 1 and not forceArray:
            row = rs[0]
            return UserDto(
                row[0], row[1],
                row[3], row[4],
                row[2]
            )

        users = [UserDto(row[0], row[1], row[2], row[3],
                         row[4])
                 for row in rs]
        return users

    def __str__(self):
        return f"user{super().__str__()}"
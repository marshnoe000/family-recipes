from libsql_client import ResultSet


class UserDto(dict):
    def __init__(self, username, passwordHash, passwordSalt, email, name):
        super().__init__(
            username=username,
            passwordHash=passwordHash,
            passwordSalt=passwordSalt,
            email=email,
            name=name,
        )

    def fromJson(json: dict):
        return UserDto(
            json.get('username'),
            json.get('passwordHash'),
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
                row[2], row[3],
                row[4]
            )

        users = [UserDto(row[0], row[1], row[2], row[3],
                         row[4])
                 for row in rs]
        return users

    def __str__(self):
        return f"user{super().__str__()}"

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value

from os import getenv

import libsql_client as libsql

from dtos.errors import DatabaseError


class BaseRepository:
    def __init__(self, isProd: bool):
        self.client = libsql.create_client_sync(
            url=getenv("DATABASE_URL"),
            auth_token=getenv("DATABASE_AUTHTOKEN")
        )

    def execute(self, stat: str, args: list[any]) -> any:
        try:
            return self.client.execute(stat, args)
        except libsql.LibsqlError as e:
            # raise DatabaseError(e.explanation)
            # TODO explanation field should exist but doesnt, use args instead
            raise DatabaseError(e.args[0])

    def __del__(self):
        if self.client:
            self.client.close()

from os import getenv

import libsql_client as libsql


class BaseRepository:
    def __init__(self, isProd: bool):
        self.client = libsql.create_client_sync(
            url=getenv("DATABASE_URL"),
            auth_token=getenv("DATABASE_AUTHTOKEN")
        )

    def __del__(self):
        if self.client:
            self.client.close()

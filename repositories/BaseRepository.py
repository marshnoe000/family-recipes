import libsql_client as libsql
import configparser

class BaseRepository:
    def __init__(self, isProd):
        config = configparser.ConfigParser()
        config.read("config.ini")
        if isProd:
            self.client = libsql.create_client_sync(
                url=config.get('database', 'url'),
                auth_token=config.get('database', 'auth_token')
            )
        else:
            self.client = libsql.create_client_sync(url="file:scripts/recipes.db")

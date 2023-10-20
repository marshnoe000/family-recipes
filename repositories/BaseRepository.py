import libsql_client as libsql

class BaseRepository:
    def __init__(self, isProd):
        if isProd:
            self.client = libsql.create_client_sync(
                url="libsql://recipes-deparr.turso.io",
                auth_token="eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIyMDIzLTEwLTE4VDAyOjI0OjMyLjEzNDM2MjU1MVoiLCJpZC"
                           "I6ImViMTdhZDMxLTZhZWYtMTFlZS05NzA3LWZhMThmYjJkYTBjNSJ9.QNkryPV--hw48Y4nFICjSVoiBwrPxRb5m_0gpwKw"
                           "DM-HsSsXzFBN7W8s8q5_uCTr5XPqOSVwi6QF9pqTO8oZCQ"
            )
        else:
            self.client = libsql.create_client_sync(url="file:scripts/recipes.db")
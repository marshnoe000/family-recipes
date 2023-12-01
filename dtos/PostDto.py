from libsql_client import ResultSet
from .errors import BadRequestError


class PostDto(dict):
    def __init__(self, id, author, recipeId, groupId, content, dateCreated, likes, tags):

        if bool(tags) and type(tags) is not list:
            raise BadRequestError("Expected array for post.tags")

        super().__init__(
            id=id,
            author=author,
            groupId=groupId,
            content=content,
            dateCreated=dateCreated,
            likes=likes,
            recipeId=recipeId,
            tags=tags,
        )

    def fromJson(json: dict):
        return PostDto(
            json.get('id'),
            json.get('author'),
            json.get('recipeId'),
            json.get('groupId'),
            json.get('content'),
            json.get('dateCreated'),
            json.get('likes'),
            json.get('tags')
        )

    def fromResultSet(rs: ResultSet, forceArray=False):
        if len(rs) == 0:
            return None

        if len(rs) == 1 and not forceArray:
            row = rs[0]
            return PostDto(
                row[0], row[1],
                row[2], row[3],
                row[4], row[5],
                row[6], row[7].split(',') if row[7] else list()
            )

        posts = [PostDto(row[0], row[1], row[2], row[3],
                         row[4], row[5], row[6], row[7].split(',') if row[7] else list())
                 for row in rs]
        return posts

    def __str__(self):
        return f"post{super().__str__()}"

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value

from libsql_client import ResultSet


class PostDto(dict):
    def __init__(self, id, author, recipeId, groupId, content, dateCreated, likes, tags):
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
                row[6], row[7]
            )

        posts = [PostDto(row[0], row[1], row[2], row[3],
                         row[4], row[5], row[6], row[7])
                 for row in rs]
        return posts

    def __str__(self):
        return f"post{super().__str__()}"

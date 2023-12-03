from libsql_client import ResultSet
import json

class CommentDto:
    def __init__(self, commentId, author, content, postId, parentId, created_at):
        self.commentId = commentId
        self.author = author
        self.content = content
        self.postId = postId
        self.parentId = parentId
        self.created_at = created_at

    def fromJson(json: dict):
        return CommentDto(
            commentId=json.get('id'),
            author=json.get('author'),
            content=json.get('content'),
            postId=json.get('postId'),
            parentId=json.get('parentId'),
            created_at=json.get('create_at')
        )

    def fromResultSet(resultSet: ResultSet, forceArray: bool):
        if len(resultSet) == 0:
            return None

        if len(resultSet) == 1 and not forceArray:
            return CommentDto(
                commentId=resultSet.rows[0][0],
                author=resultSet.rows[0][1],
                content=resultSet.rows[0][2],
                postId=resultSet.rows[0][3],
                parentId=resultSet.rows[0][4],
                created_at=resultSet.rows[0][5])

        return [CommentDto(
                commentId=row[0],
                author=row[1],
                content=row[2],
                postId=row[3],
                parentId=row[4],
                created_at=row[5]
            ) for row in resultSet.rows]

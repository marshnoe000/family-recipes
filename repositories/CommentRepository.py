from datetime import datetime

from .BaseRepository import BaseRepository
from libsql_client import ResultSet
from dtos import CommentDto
class CommentRepository(BaseRepository):
    INSERT_COMMENT_STATEMENT = "insert into comment(author, content, post_id, parent_id, created_at) values (?,?,?,?,datetime())"
    QUERY_COMMENTS_BY_POSTID_STATEMENT = "select id, author, content, post_id, parent_id, created_at from comment where post_id = ?"
    DELETE_COMMENT_BY_ID_STATEMENT = "delete from comment where id = ?"
    QUERY_SINGLE_COMMENT_BY_ID_STATEMENT = "select id, author, content, post_id, parent_id, created_at from comment where id = ?"

    def __init__(self):
        super().__init__()

    def insertComment(self, commentDto: CommentDto) -> ResultSet:
        return self.client.execute(CommentRepository.INSERT_COMMENT_STATEMENT, [commentDto.author,
                                                                                commentDto.content, commentDto.postId,
                                                                                commentDto.parentId])

    def getCommentById(self, commentId) -> ResultSet:
        return self.client.execute(CommentRepository.QUERY_SINGLE_COMMENT_BY_ID_STATEMENT, [commentId])
    def getCommentsByPostId(self, postId: int) -> ResultSet:
        return self.client.execute(CommentRepository.QUERY_COMMENTS_BY_POSTID_STATEMENT, [postId])

    def deleteCommentById(self, commentId: int) -> ResultSet:
        return self.client.execute(CommentRepository.DELETE_COMMENT_BY_ID, [commentId])

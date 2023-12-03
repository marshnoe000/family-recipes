from libsql_client import ResultSet

from dtos import CommentDto
from repositories.CommentRepository import CommentRepository
from dtos.responses import *
class CommentService:
    def __init__(self):
        self.commentRepository = CommentRepository()

    def postComment(self, commentDto: CommentDto) -> CreateResponse:
        resultSet: ResultSet = self.commentRepository.insertComment(commentDto)
        return CreateResponse(status=201, id=resultSet.last_insert_rowid)

    def getComment(self, commentId: int) -> DataResponse:
        resultSet: ResultSet = self.commentRepository.getCommentById(commentId)
        return DataResponse(status=200, data=CommentDto.fromResultSet(resultSet=resultSet, forceArray=False))

    def getPostComments(self, postId: int) -> DataResponse:
        resultSet: ResultSet = self.commentRepository.getCommentsByPostId(postId)
        comments: list[CommentDto] = CommentDto.fromResultSet(resultSet=resultSet, forceArray=True)
        return DataResponse(status=200, data=comments)

    def deleteComment(self, commentId: int) -> DeleteResponse:
        resultSet: ResultSet = self.commentRepository.deleteCommentById(commentId)
        return DeleteResponse(status=200, rowsAffected=resultSet.rows_affected)
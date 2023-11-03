from flask import current_app as app

from repositories import PostRepository
from dtos import PostDto
from dtos.responses import DataResponse
from dtos.errors import BadRequestError


def validateCreatePost(post: PostDto):
    if post["author"] is None or len(post["author"]) == 0:
        raise BadRequestError("Expected post author")

    if post["recipeId"] is None:
        raise BadRequestError("Expected post recipeId")

    if post["groupId"] is None:
        raise BadRequestError("Expected post groupId")


class PostService:
    def __init__(self, isProd=False):
        self.postRepo = PostRepository(isProd)

    def makePost(self, post: PostDto) -> DataResponse:
        app.logger.info(f"got post: {post}")
        validateCreatePost(post)
        insertedId = self.postRepo.insertPost(post)
        res = DataResponse(201, {"id": insertedId})

        return res

    def getPost(self, id: int) -> DataResponse:
        post = self.postRepo.getPostById(id)
        res = DataResponse(200, {"post": post})
        return res

    def getUserPosts(self, username: str) -> DataResponse:
        posts = self.postRepo.getPostsByUser(username)
        res = DataResponse(200, {"posts": posts})

        return res

    def getGroupPosts(self, groupId: int) -> DataResponse:
        posts = self.postRepo.getPostsByGroup(groupId)
        res = DataResponse(200, {"posts": posts})

        return res

    def deletePost(self, id: int) -> DataResponse:
        rowsAffected = self.postRepo.deletePostById(id)
        res = DataResponse(200, {"rowsAffected": rowsAffected})

        return res

from flask import current_app as app

from repositories import PostRepository
from dtos import PostDto
from dtos.responses import DataResponse


# TODO make error classes?
def validateCreatePost(post: PostDto):
    if not post["author"] or len(post["author"]) == 0:
        # raise BadRequestError("Missing post author")
        raise Exception("Missing post author")

    if not post["recipeId"]:
        # raise BadRequestError("Missing post recipeId")
        raise Exception("Missing post recipeId")
    if not post["groupId"]:
        # raise BadRequestError("Missing post groupId")
        raise Exception("Missing post groupId")


class PostService:
    def __init__(self, isProd=False):
        self.postRepo = PostRepository(isProd)

    def makePost(self, post: PostDto) -> DataResponse:
        app.logger.info(f"got post: {post}")
        validateCreatePost(post)
        insertedId, success = self.postRepo.insertPost(post)
        res = None
        if success:
            res = DataResponse(200, {"id": insertedId})
        else:
            # TODO Error handling
            res = {"status": 500, "message": "TODO: Database error"}

        return res

    def getPost(self, id: int) -> DataResponse:
        post, success = self.postRepo.getPostById(id)

        res = None
        if success:
            res = DataResponse(200, {"post": post})
        else:
            # TODO Error handling
            res = {"status": 500, "message": "TODO: Database error"}
        return res

    def getUserPosts(self, username: str) -> DataResponse:
        posts, success = self.postRepo.getPostsByUser(username)

        res = None
        if success:
            res = DataResponse(200, {"posts": posts})
        else:
            # TODO Error handling
            res = {"status": 500, "message": "TODO: Database error"}

        return res

    def getGroupPosts(self, groupId: int) -> DataResponse:
        posts, success = self.postRepo.getPostsByGroup(groupId)

        res = None
        if success:
            res = DataResponse(200, {"posts": posts})
        else:
            # TODO error handling, Error response?
            res = {"status": 500, "message": "TODO: Database error"}

        return res

    def deletePost(self, id: int) -> DataResponse:
        rowsAffected, success = self.postRepo.deletePostById(id)

        res = None
        if success:
            res = DataResponse(200, {"rowsAffected": rowsAffected})
        else:
            # TODO error handling, Error response?
            res = {"status": 500, "message": "TODO: Database error"}

        return res

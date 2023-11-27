from flask import current_app as app

from repositories import PostRepository
from dtos import PostDto
from dtos.responses import DataResponse, DeleteResponse, CreateResponse
from dtos.errors import BadRequestError


def validateNewPost(post: PostDto):
    badVal = None
    if post.author is None or len(post.author) == 0:
        badVal = "author"

    if post.recipeId is None:
        badVal = "recipeId"

    if post.groupId is None:
        badVal = "groupId"

    if badVal is not None:
        raise BadRequestError(f"Need post.{badVal} to create post")


class PostService:
    def __init__(self):
        self.postRepo = PostRepository()

    def makePost(self, post: PostDto) -> CreateResponse:
        validateNewPost(post)
        app.logger.debug(f"creating {post}...")
        insertedId = self.postRepo.insertPost(post)
        res = CreateResponse(201, insertedId)

        return res

    def getPost(self, id: int, embedRecipe: bool) -> DataResponse:
        post = self.postRepo.getPostById(id, embedRecipe)
        res = DataResponse(200, post)

        return res

    def getUserPosts(self, username: str, embedRecipe: bool) -> DataResponse:
        posts = self.postRepo.getPostsByUser(username, embedRecipe)
        res = DataResponse(200, posts)

        return res

    def getGroupPosts(self, groupId: int, embedRecipe: bool) -> DataResponse:
        posts = self.postRepo.getPostsByGroup(groupId, embedRecipe)
        res = DataResponse(200, posts)

        return res

    def deletePost(self, id: int) -> DeleteResponse:
        rowsAffected = self.postRepo.deletePostById(id)
        res = DeleteResponse(200, rowsAffected)

        return res

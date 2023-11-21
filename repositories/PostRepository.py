from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import PostDto


class PostRepository(BaseRepository):
    INSERT_POST = "insert into post (author, recipe_id, group_id, content, created_at, likes, tags) values (?, ?, ?, ?, datetime(), 0, ?)"
    SELECT_ALL_BY_ID = "select * from post where post.id = ?"
    SELECT_ALL_BY_USER = "select * from post where post.author = ?"
    SELECT_ALL_BY_GROUP = "select * from post where post.group_id = ?"
    DELETE_BY_ID = "delete from post where post.id = ?"
    JOIN_WITH_RECIPE = " join recipe on post.recipe_id = recipe.id"

    def __init__(self):
        super().__init__()

    def insertPost(self, post: PostDto) -> int:

        if type(post.tags) is list:
            post.tags = ",".join(post.tags)

        rs: ResultSet = self.execute(
            PostRepository.INSERT_POST,
            [post.author, post.recipeId,
             post.groupId, post.content,
             post.tags])

        return rs.last_insert_rowid

    def getPostById(self, id: int, embedRecipe: bool) -> PostDto:
        query: str = PostRepository.SELECT_ALL_BY_ID
        if embedRecipe:
            query += PostRepository.JOIN_WITH_RECIPE

        rs: ResultSet = self.execute(query, [id])

        post = PostDto.fromResultSet(rs)
        return post

    def getPostsByUser(self, username: str, embedRecipe: bool) -> list[PostDto]:
        query: str = PostRepository.SELECT_ALL_BY_USER
        if embedRecipe:
            query += PostRepository.JOIN_WITH_RECIPE

        rs: ResultSet = self.execute(query, [username])

        posts = PostDto.fromResultSet(rs, forceArray=True)
        return posts

    def getPostsByGroup(self, groupId: int, embedRecipe) -> list[PostDto]:
        query: str = PostRepository.SELECT_ALL_BY_GROUP
        if embedRecipe:
            query += PostRepository.JOIN_WITH_RECIPE

        rs: ResultSet = self.execute(query, [groupId])

        posts = PostDto.fromResultSet(rs, forceArray=True)
        return posts

    def deletePostById(self, id: int) -> int:
        rs: ResultSet = self.execute(
            PostRepository.DELETE_BY_ID,
            [id])

        return rs.rows_affected

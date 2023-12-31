from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import PostDto, RecipeDto


class PostRepository(BaseRepository):
    INSERT_POST = "insert into post (author, recipe_id, group_id, content, created_at, likes, tags) values (?, ?, ?, ?, datetime(), 0, ?)"
    SELECT_ALL_BY_ID = "select * from post where post.id = ?"
    SELECT_ALL_BY_USER = "select * from post where post.author = ?"
    SELECT_ALL_BY_GROUP = "select * from post where post.group_id = ?"
    SELECT_ALL_BY_GROUP_LIST = "select * from post where post.group_id in ({})"
    DELETE_BY_ID = "delete from post where post.id = ?"
    SORT_MOST_RECENT = " order by created_at desc"
    JOIN_RECIPE = " join recipe on post.recipe_id = recipe.id "

    def __init__(self):
        super().__init__()

    def withJoin(self, query: str, join: str) -> str:
        whereIdx = query.find('where')
        if whereIdx == -1:
            whereIdx = len(query)
        return query[:whereIdx] + join + query[whereIdx:]

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
            query = self.withJoin(query, PostRepository.JOIN_RECIPE)

        rs: ResultSet = self.execute(query, [id])
        post = PostDto.fromResultSet(rs)

        if embedRecipe and post is not None:
            # `*` on a list is like the js `...` operator
            post.recipe = RecipeDto(*(rs[0][8:]))
            del post["recipeId"]

        return post

    def getPostsByUser(self, username: str, embedRecipe: bool, sortDate: bool = False) -> list[PostDto]:
        query: str = PostRepository.SELECT_ALL_BY_USER
        if embedRecipe:
            query = self.withJoin(query, PostRepository.JOIN_RECIPE)
        if sortDate:
            query += PostRepository.SORT_MOST_RECENT

        rs: ResultSet = self.execute(query, [username])
        posts = PostDto.fromResultSet(rs, forceArray=True)

        if embedRecipe and posts is not None:
            for row, post in zip(rs.rows, posts):
                post.recipe = RecipeDto(*row[8:])
                del post["recipeId"]

        return posts

    def getPostsByGroup(self, groupId: int, embedRecipe: bool, sortDate: bool = False) -> list[PostDto]:
        query = PostRepository.SELECT_ALL_BY_GROUP
        if embedRecipe:
            query = self.withJoin(query, PostRepository.JOIN_RECIPE)
        if sortDate:
            query += PostRepository.SORT_MOST_RECENT

        rs: ResultSet = self.execute(query, [groupId])
        posts = PostDto.fromResultSet(rs, forceArray=True)

        if embedRecipe and posts is not None:
            for row, post in zip(rs.rows, posts):
                post.recipe = RecipeDto(*row[8:])
                del post["recipeId"]

        return posts

    def getPostsByGroupList(self, groups: list[int], embedRecipe: bool, sortDate: bool = False) -> list[PostDto]:
        query = PostRepository.SELECT_ALL_BY_GROUP_LIST
        if embedRecipe:
            query = self.withJoin(query, PostRepository.JOIN_RECIPE)
        if sortDate:
            query += PostRepository.SORT_MOST_RECENT

        groupstr = groups.__str__().strip("[]")
        rs: ResultSet = self.execute(
            query.format(groupstr),
            None)
        posts = PostDto.fromResultSet(rs, forceArray=True)

        if embedRecipe and posts is not None:
            for row, post in zip(rs.rows, posts):
                post.recipe = RecipeDto(*row[8:])
                del post["recipeId"]

        return posts

    def deletePostById(self, id: int) -> int:
        rs: ResultSet = self.execute(
            PostRepository.DELETE_BY_ID,
            [id])

        return rs.rows_affected

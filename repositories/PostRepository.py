from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import PostDto


# TODO better error handling
class PostRepository(BaseRepository):
    INSERT_POST = "insert into post (author, recipe_id, group_id, content, created_at, likes, tags) values (?, ?, ?, ?, datetime(), 0, ?)"
    SELECT_ALL_BY_ID = "select * from post where post.id = ?"
    SELECT_ALL_BY_USER = "select * from post where post.author = ?"
    SELECT_ALL_BY_GROUP = "select * from post where post.group_id = ?"
    DELETE_BY_ID = "delete from post where post.id = ?"

    def __init__(self, isProd: bool):
        super().__init__(isProd)

    def insertPost(self, post: PostDto) -> (int, bool):
        try:
            rs = self.client.execute(PostRepository.INSERT_POST,
                                     [post["author"], post["recipeId"],
                                      post["groupId"], post["content"],
                                      post["tags"]])

            return rs.last_insert_rowid, True
        except Exception as e:
            print(e)
            return -1, False

    def getPostById(self, id: int) -> (PostDto, bool):
        try:
            rs: ResultSet = self.client.execute(
                PostRepository.SELECT_ALL_BY_ID,
                [id])

            post = PostDto.fromResultSet(rs)
            return (post, True)
        except Exception as e:
            print(e)
            return (None, False)

    def getPostsByUser(self, username: str) -> (list[PostDto], bool):
        try:
            rs: ResultSet = self.client.execute(
                PostRepository.SELECT_ALL_BY_USER,
                [username])

            posts = PostDto.fromResultSet(rs)
            return (posts, True)
        except Exception as e:
            print(e)
            return (None, False)

    def getPostsByGroup(self, groupId: int) -> (list[PostDto], bool):
        try:
            rs: ResultSet = self.client.execute(
                PostRepository.SELECT_ALL_BY_GROUP,
                [groupId])

            posts = PostDto.fromResultSet(rs)
            return (posts, True)
        except Exception as e:
            print(e)
            return (None, False)

    def deletePostById(self, id: int) -> (int, bool):
        try:
            rs: ResultSet = self.client.execute(
                PostRepository.DELETE_BY_ID,
                [id])

            return (rs.rows_affected, True)
        except Exception as e:
            print(e)
            return (0, False)

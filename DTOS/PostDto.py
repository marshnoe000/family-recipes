class PostDto:
    def __init__(self, postId, authorId, dateCreated, likes, recipeId, tags):
        self.postId = postId
        self.authorId = authorId
        self.dateCreated = dateCreated
        self.likes = likes
        self.recipeId = recipeId
        self.tags = tags

class PostDto:
    def __init__(self, pid, authorId, dateCreated, likes, recipeId, tags):
        self.pid = pid
        self.authorId = authorId
        self.dateCreated = dateCreated
        self.likes = likes
        self.recipeId = recipeId
        self.tags = tags

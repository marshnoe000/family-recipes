class RecipeDto:
    def __init__(self, rid, title, description, ingredients, instructions, difficultyLevel, image, foodType,
                 recipeSource):
        self.rid = rid
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.difficultyLevel = difficultyLevel
        self.image = image
        self.foodType = foodType
        self.recipeSource = recipeSource

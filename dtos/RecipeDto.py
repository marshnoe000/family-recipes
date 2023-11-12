from libsql_client import ResultSet
import json


class RecipeDto:
    def __init__(self, recipeId, title, description, ingredients, instructions, difficultyLevel, image, foodType,
                 recipeSource):
        self.recipeId = recipeId
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.difficultyLevel = difficultyLevel
        self.image = image
        self.foodType = foodType
        self.recipeSource = recipeSource

    def fromJson(json: dict):
        return RecipeDto(
            recipeId=json.get("id"),
            title=json.get("title"),
            description=json.get("description"),
            ingredients=json.get("ingredients"),
            instructions=json.get("instructions"),
            difficultyLevel=json.get("difficultyLevel"),
            image=json.get("image"),
            foodType=json.get("foodType"),
            recipeSource=json.get("recipeSource")
        )

    def fromResultSet(resultSet: ResultSet, forceArray: bool = False):
        if len(resultSet) == 0:
            return None

        if len(resultSet) == 1 and not forceArray:
            return RecipeDto(recipeId=resultSet.rows[0][0],
                             title=resultSet.rows[0][1],
                             description=resultSet.rows[0][2],
                             ingredients=resultSet.rows[0][3].split(','),
                             instructions=resultSet.rows[0][4],
                             difficultyLevel=resultSet.rows[0][5],
                             image=resultSet.rows[0][6],
                             foodType=resultSet.rows[0][7],
                             recipeSource=resultSet.rows[0][8])

        return [RecipeDto(
            recipeId=row[0],
            title=row[1],
            description=row[2],
            ingredients=row[3].split(','),
            instructions=row[4],
            difficultyLevel=row[5],
            image=row[6],
            foodType=row[7],
            recipeSource=row[8]
        ) for row in resultSet.rows]

    def __str__(self):
        return f"user{super().__str__()}"

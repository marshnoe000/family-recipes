from .BaseRepository import BaseRepository
from dtos import RecipeDto
from libsql_client import ResultSet

import base64


class RecipeRepository(BaseRepository):
    GET_ALL_RECIPES_STATEMENT = 'select id, title, description, ingredients, instructions, difficulty_level, image, food_type, recipe_source from recipe'

    INSERT_RECIPE_STATEMENT = "insert into recipe (title, description, ingredients, instructions, difficulty_level, image, food_type, recipe_source) values (?,?,?,?,?,?,?,?)"

    GET_RECIPE_BY_ID_STATEMENT = "select id, title, description, ingredients, instructions, difficulty_level, image, food_type, recipe_source from recipe where id = ?"

    DELETE_RECIPE_BY_ID_STATEMENT = "delete from recipe where id = ?"

    def __init__(self):
        super().__init__()

    def getAllRecipes(self) -> ResultSet:
        result_set = self.client.execute(RecipeRepository.GET_ALL_RECIPES_STATEMENT)

        return result_set

    def insertRecipe(self, recipeDto: RecipeDto) -> ResultSet:
        unencodedImage = base64.b64decode(recipeDto.image)
        resultSet: ResultSet = self.client.execute(RecipeRepository.INSERT_RECIPE_STATEMENT,
                                                   [recipeDto.title, recipeDto.description,
                                                    ','.join(recipeDto.ingredients) if recipeDto.ingredients is not None else '',
                                                    recipeDto.instructions,
                                                    recipeDto.difficultyLevel, unencodedImage, recipeDto.foodType,
                                                    recipeDto.recipeSource])
        return resultSet

    def getRecipeById(self, recipeId: int) -> ResultSet:
        resultSet: ResultSet = self.client.execute(RecipeRepository.GET_RECIPE_BY_ID_STATEMENT, [recipeId])
        return resultSet

    def deleteRecipeById(self, recipeId: int) -> ResultSet:
        resultSet: ResultSet = self.client.execute(RecipeRepository.DELETE_RECIPE_BY_ID_STATEMENT, [recipeId])
        return resultSet

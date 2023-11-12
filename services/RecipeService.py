from libsql_client import ResultSet

from dtos import RecipeDto
from repositories.RecipeRepository import RecipeRepository
from dtos.RecipeDto import RecipeDto
from dtos.responses import *

class RecipeService:
    def __init__(self):
        self.recipeRepository = RecipeRepository()

    def getAllRecipes(self) -> DataResponse:
        resultSet: ResultSet = self.recipeRepository.getAllRecipes()
        recipes = RecipeDto.fromResultSet(resultSet=resultSet, forceArray=True)
        return DataResponse(200, recipes)

    def postRecipe(self, recipe: RecipeDto) -> CreateResponse:
        resultSet: ResultSet = self.recipeRepository.insertRecipe(recipe)
        return CreateResponse(200, resultSet.last_insert_rowid)

    def getRecipeById(self, recipeId) -> DataResponse:
        resultSet: ResultSet = self.recipeRepository.getRecipeById(recipeId)
        recipe = RecipeDto.fromResultSet(resultSet=resultSet, forceArray=False)
        return DataResponse(200, recipe)

    def deleteRecipe(self, recipeId) -> DeleteResponse:
        resultSet: ResultSet = self.recipeRepository.deleteRecipeById(recipeId)
        return DeleteResponse(200, resultSet.rows_affected)

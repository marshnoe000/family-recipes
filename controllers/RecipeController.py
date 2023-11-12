from flask import Blueprint, jsonify, request
from services.RecipeService import RecipeService
from dtos import RecipeDto
from dtos.responses import *
import json

recipe_blueprint = Blueprint('recipe', __name__)


@recipe_blueprint.route('/recipe/<int:recipeId>', methods=['GET'])
def getRecipeById(recipeId: int):
    recipeService = RecipeService()
    res: dict = recipeService.getRecipeById(recipeId)

    json_res = json.dumps(res, default=lambda o: o.__dict__)
    return json_res, res['status']


@recipe_blueprint.route('/recipe', methods=['GET'])
def getAllRecipes():
    recipeService = RecipeService()

    res: DataResponse = recipeService.getAllRecipes()

    json_res = json.dumps(res, default=lambda o: o.__dict__)

    return json_res, res['status']


@recipe_blueprint.route('/recipe', methods=['POST'])
def postRecipe():
    data = request.get_json()

    recipeService = RecipeService()

    recipe = RecipeDto.fromJson(data)

    res = recipeService.postRecipe(recipe)

    json_res = json.dumps(res, default=lambda o: o.__dict__)

    return json_res, res['status']


@recipe_blueprint.route('/recipe/<int:recipeId>', methods=['DELETE'])
def deleteRecipe(recipeId: int):
    recipeService = RecipeService()
    res = recipeService.deleteRecipe(recipeId)
    json_res = json.dumps(res, default=lambda o: o.__dict__)
    return json_res, res['status']


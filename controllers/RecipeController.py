from flask import Blueprint, jsonify

recipe_blueprint = Blueprint('recipe', __name__)


@recipe_blueprint.route('/recipe', methods=['GET'])
def getRecipe():
    data = {'message': 'This is the response from the recipe endpoint'}
    return jsonify(data)

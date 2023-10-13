from flask import Flask
from controllers.UserController import user_blueprint
from controllers.PostController import post_blueprint
from controllers.RecipeController import recipe_blueprint
from controllers.GroupController import group_blueprint

app = Flask(__name__)

# Register the blueprints (controllers)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(group_blueprint)

if __name__ == '__main__':
    app.run()

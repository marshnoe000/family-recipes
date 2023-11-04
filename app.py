import os
import logging
from dotenv import load_dotenv

from flask import Flask
from controllers.UserController import user_blueprint
from controllers.PostController import post_blueprint
from controllers.RecipeController import recipe_blueprint
from controllers.GroupController import group_blueprint
from controllers.ErrorController import error_blueprint


app = Flask(__name__)
app.logger.setLevel(logging.INFO)

if load_dotenv(os.getenv("ENV_PATH")):
    app.logger.info(f"Loaded env from path: {os.getenv('ENV_PATH')}")
else:
    app.logger.warn(f"Unable to load env from path: {os.getenv('ENV_PATH')}")


loglevel = logging.INFO
if os.getenv("LOG_LEVEL"):
    match os.getenv("LOG_LEVEL").lower():
        case "debug":
            loglevel = logging.DEBUG
        case "info":
            loglevel = logging.INFO
        case "warn":
            loglevel = logging.WARN
        case "error":
            loglevel = logging.ERRO
        case "critical":
            loglevel = logging.CRITICAL
        case _:
            loglevel = logging.INFO

    app.logger.setLevel(loglevel)
    del loglevel


# Register the blueprints (controllers)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(group_blueprint)
app.register_blueprint(error_blueprint)

if __name__ == '__main__':
    app.run()

from flask import Blueprint, jsonify, current_app as app
from dtos.responses import ErrorResponse

error_blueprint = Blueprint('error', __name__)


@error_blueprint.app_errorhandler(Exception)
def handle_app_error(e):
    app.logger.error("%s: %s", type(e).__name__, e)
    res: dict = ErrorResponse(e)
    return jsonify(res), res.status

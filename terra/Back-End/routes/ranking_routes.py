from flask import Blueprint
from controllers.ranking_controller import create_ranking

ranking_bp = Blueprint("ranking", __name__, url_prefix="/ranking")

# POST /ranking → cria um novo registro no ranking
ranking_bp.route("/", methods=["POST"])(create_ranking)

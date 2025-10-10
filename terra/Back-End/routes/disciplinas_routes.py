from flask import Blueprint
from controllers.disciplinas_controller import create_disciplina

disciplinas_bp = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

disciplinas_bp.route("/", methods=["POST"])(create_disciplina)

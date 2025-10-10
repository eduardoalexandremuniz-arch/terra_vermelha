from flask import Blueprint
from controllers.cursos_controller import create_curso

cursos_bp = Blueprint("cursos", __name__, url_prefix="/cursos")

# POST /cursos → cria um novo curso
cursos_bp.route("/", methods=["POST"])(create_curso)

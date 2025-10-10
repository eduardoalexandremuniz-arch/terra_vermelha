from flask import Blueprint
from controllers.alunos_controller import create_aluno, get_alunos, update_aluno, delete_aluno

alunos_bp = Blueprint("alunos", __name__, url_prefix="/alunos")

alunos_bp.route("/", methods=["POST"])(create_aluno)
alunos_bp.route("/", methods=["GET"])(get_alunos)
alunos_bp.route("/<id>", methods=["PUT"])(update_aluno)
alunos_bp.route("/<id>", methods=["DELETE"])(delete_aluno)

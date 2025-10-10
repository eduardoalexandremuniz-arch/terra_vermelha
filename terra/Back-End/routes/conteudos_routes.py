from flask import Blueprint
from controllers.conteudos_controller import create_conteudo

conteudos_bp = Blueprint("conteudos", __name__, url_prefix="/conteudos")

# POST /conteudos → cria um novo conteúdo
conteudos_bp.route("/", methods=["POST"])(create_conteudo)

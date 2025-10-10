from flask import jsonify, request
from utils.csv_handler import write_csv
import uuid

CSV_PATH = "data/cursos.csv"
FIELDS = ["id", "nome", "descricao"]

def create_curso():
    data = request.get_json()
    novo = {
        "id": str(uuid.uuid4()),
        "nome": data.get("nome"),
        "descricao": data.get("descricao", "")
    }

    if not novo["nome"]:
        return jsonify({"erro": "Nome do curso é obrigatório"}), 400

    write_csv(CSV_PATH, novo, FIELDS)
    return jsonify({"mensagem": "Curso cadastrado com sucesso", "dados": novo}), 201

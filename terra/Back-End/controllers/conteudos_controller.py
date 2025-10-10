from flask import jsonify, request
from utils.csv_handler import write_csv
import uuid

CSV_PATH = "data/conteudos.csv"
FIELDS = ["id", "titulo", "descricao", "disciplina", "tipo", "url"]

def create_conteudo():
    data = request.get_json()
    novo = {
        "id": str(uuid.uuid4()),
        "titulo": data.get("titulo"),
        "descricao": data.get("descricao", ""),
        "disciplina": data.get("disciplina"),
        "tipo": data.get("tipo", "apostila"),
        "url": data.get("url", "")
    }

    if not novo["titulo"] or not novo["disciplina"]:
        return jsonify({"erro": "Título e disciplina são obrigatórios"}), 400

    write_csv(CSV_PATH, novo, FIELDS)
    return jsonify({"mensagem": "Conteúdo cadastrado com sucesso", "dados": novo}), 201

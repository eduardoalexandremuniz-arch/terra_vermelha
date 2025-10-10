from flask import jsonify, request
from utils.csv_handler import write_csv
import uuid

CSV_PATH = "data/disciplinas.csv"
FIELDS = ["id", "nome", "curso", "carga_horaria"]

def create_disciplina():
    data = request.get_json()
    nova = {
        "id": str(uuid.uuid4()),
        "nome": data.get("nome"),
        "curso": data.get("curso"),
        "carga_horaria": data.get("carga_horaria", "0")
    }

    if not nova["nome"] or not nova["curso"]:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    write_csv(CSV_PATH, nova, FIELDS)
    return jsonify({"mensagem": "Disciplina cadastrada com sucesso", "dados": nova}), 201

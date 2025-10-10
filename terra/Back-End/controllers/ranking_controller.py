from flask import jsonify, request
from utils.csv_handler import write_csv
import uuid

CSV_PATH = "data/ranking.csv"
FIELDS = ["id", "id_aluno", "nome", "pontos_jogo", "monstros_vencidos"]

def create_ranking():
    data = request.get_json()
    novo = {
        "id": str(uuid.uuid4()),
        "id_aluno": data.get("id_aluno"),
        "nome": data.get("nome"),
        "pontos_jogo": data.get("pontos_jogo", "0"),
        "monstros_vencidos": data.get("monstros_vencidos", "0")
    }

    if not novo["id_aluno"] or not novo["nome"]:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    write_csv(CSV_PATH, novo, FIELDS)
    return jsonify({"mensagem": "Ranking cadastrado com sucesso", "dados": novo}), 201

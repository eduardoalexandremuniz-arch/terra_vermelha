from flask import jsonify, request
from utils.csv_handler import write_csv, read_csv, update_csv, delete_csv
import uuid
import hashlib

CSV_PATH = "data/alunos.csv"
FIELDS = ["id", "nome", "cpf", "data_nascimento", "telefone", "email", "senha", "genero", "curso", "disciplina", "progresso", "ranking"]

def hash_senha(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def create_aluno():
    data = request.get_json()

    # Validação campos obrigatórios
    obrigatorios = ["nome", "cpf", "email", "senha"]
    for campo in obrigatorios:
        if not data.get(campo):
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    senha_hashed = hash_senha(data["senha"])

    novo = {
        "id": str(uuid.uuid4()),
        "nome": data.get("nome"),
        "cpf": data.get("cpf"),
        "data_nascimento": data.get("data_nascimento", ""),
        "telefone": data.get("telefone", ""),
        "email": data.get("email"),
        "senha": senha_hashed,
        "genero": data.get("genero", ""),
        "curso": data.get("curso", ""),
        "disciplina": data.get("disciplina", ""),
        "progresso": data.get("progresso", "0"),
        "ranking": data.get("ranking", "0")
    }

    write_csv(CSV_PATH, novo, FIELDS)
    return jsonify({"mensagem": "Aluno cadastrado com sucesso", "dados": novo}), 201


# GET - listar todos alunos
def get_alunos():
    alunos = read_csv(CSV_PATH)
    for aluno in alunos:
        aluno.pop("senha", None)  # não retornar a senha
    return jsonify(alunos), 200

# PUT - atualizar aluno pelo id
def update_aluno(id):
    data = request.get_json()

    # Se senha for alterada, hasheie antes
    if "senha" in data:
        data["senha"] = hash_senha(data["senha"])

    atualizado = update_csv(CSV_PATH, id, data)
    if atualizado:
        return jsonify({"mensagem": "Aluno atualizado com sucesso"}), 200
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404

# DELETE - remover aluno pelo id
def delete_aluno(id):
    removido = delete_csv(CSV_PATH, id)
    if removido:
        return jsonify({"mensagem": "Aluno removido com sucesso"}), 200
    else:
        return jsonify({"erro": "Aluno não encontrado"}), 404

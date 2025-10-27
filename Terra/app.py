from flask import Flask, render_template, request, redirect
import csv, os
from datetime import datetime


app = Flask(__name__)


DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

def inicializar_csv(nome_arquivo, cabecalho):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho):
        with open(caminho, mode= "w", newline= "", enconding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=cabecalho)
            escritor.writeheader()

def salvar_csv(nome_arquivo, dados, cabecalho):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    arquivo_existe = os.path.isfile(caminho)
    with open(caminho, mode="a", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=cabecalho)
        if not arquivo_existe:
            escritor.writeheader()
        escritor.writerow(dados)

def ler_csv(nome_arquivo):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho):
        return []
    with open(caminho, newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        return list(leitor)

@app.route("/")
def index():
    return render_template("index.html")        

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/sobre_nos")
def sobre_nos():
    return render_template("sobre_nos.html")

# ---------- CURSOS ----------
@app.route("/cursos", methods=["GET", "POST"])
def cursos():
    arquivo = "cursos.csv"
    cabecalho = ["id", "nome_curso", "descricao", "modalidade", "requisitos", "duracao", "data_registro"]

    if request.method == "POST":
        dados = {
            "id": str(len(ler_csv(arquivo)) + 1),
            "nome_curso": request.form["nome_curso"],
            "descricao": request.form["descricao"],
            "modalidade": request.form["modalidade"],
            "requisitos": request.form["requisitos"],
            "duracao": request.form["duracao"],
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cursos")

    registros = ler_csv(arquivo)
    return render_template("cursos.html", registros=registros)




# ---------- ALUNOS ----------
@app.route("/alunos", methods=["GET", "POST"])
def alunos():
    arquivo = "alunos.csv"
    arquivo_cursos = "cursos.csv"
    cabecalho = ["id", "nome", "cpf", "data_nascimento", "telefone", "email",
                 "senha", "repetir_senha", "genero", "curso_id", "data_registro"]
    tipo_genero = {"Masculino", "Feminino", "Outro", "Prefiro não responder"}
    
    cursos = ler_csv(arquivo_cursos)
    
    if request.method == "POST":
        dados ={
            "id": str(len(ler_csv(arquivo)) + 1),
            "nome": request.form.get("nome", "").strip(),
            "cpf": request.form.get("cpf", "").strip(),
            "data_nascimento": request.form.get("data_nascimento", "").strip(),
            "telefone": request.form.get("telefone", "").strip(),
            "email": request.form.get("email", "").strip(),
            "senha": request.form.get("senha", "").strip(),
            "repetir_senha": request.form.get("repetir_senha", "").strip(),
            "genero": request.form.get("genero", "").strip(),
            "curso_id": request.form.get("curso_id", "").strip(),
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }        
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/alunos")
    
    alunos = ler_csv(arquivo)
    
    for aluno in alunos:
        curso_nome = ""
        for curso in cursos:
            if curso["id"] == aluno["curso_id"]:
                curso_nome = curso["nome_curso"]
                break
        aluno["curso_nome"] = curso_nome if curso_nome else "Curso não encontrado"

    registros = ler_csv(arquivo)
    return render_template("alunos.html", registros=registros, cursos=cursos)

# ---------- DISCIPLINAS ----------
@app.route("/disciplinas", methods=["GET", "POST"])
def disciplinas():
    arquivo = "disciplinas.csv"
    cabecalho = ["id", "nome_materia", "descricao", "carga_horaria", "curso_id", "data_registro"]
    arquivo_cursos = "cursos.csv"
    
    cursos = ler_csv(arquivo_cursos)
     
    if request.method == "POST":
        dados = {
            "id": str(len(ler_csv(arquivo)) + 1),
            "nome_materia": request.form["nome_materia"],
            "descricao": request.form["descricao"],
            "carga_horaria": request.form["duracao"],         
            "curso_id": request.form["curso_id"],
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/disciplinas")
    
    disciplinas = ler_csv(arquivo)
    
    for disciplina in disciplinas:
        curso_nome = ""
        for curso in cursos:
            if curso["id"] == disciplina["curso_id"]:
                curso_nome = curso["nome_curso"]
                break
        disciplina["curso_nome"] = curso_nome if curso_nome else "Curso não encontrado"

    registros = ler_csv(arquivo)
    return render_template("disciplinas.html", registros=registros, cursos=cursos)


# ---------- CONTEÚDOS ----------
@app.route("/conteudos", methods=["GET", "POST"])
def conteudos():
    arquivo = "conteudos.csv"
    cabecalho = ["id","titulo","descricao", "material_apoio", "video", "atividade", "id_disciplina", "data_registro"]
    arquivo_disciplina = "disciplinas.csv"
    
    disciplinas = ler_csv(arquivo_disciplina)
    
    if request.method == "POST":
        dados = {
            "id": str(len(ler_csv(arquivo)) + 1),
            "titulo":request.form["titulo"],
            "descricao": request.form["descricao"],
            "material_apoio": request.form["material_apoio"],
            "video": request.form["video"],
            "atividade": request.form["atividade"],
            "id_disciplina": request.form["id_disciplina"],
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/conteudos")
    
    conteudos = ler_csv(arquivo)
    
    for conteudo in conteudos:
        nome_materia = ""
        for disciplina in disciplinas:
            if disciplina["id"] == conteudo["id_disciplina"]:
                nome_materia = disciplina["nome_materia"]
                break
        conteudo["nome_materia"] = nome_materia if nome_materia else "Disciplina não encontrada"


    registros = ler_csv(arquivo)
    return render_template("conteudos.html", registros=registros, disciplinas=disciplinas)

# ---------- RANKING ----------
@app.route("/ranking", methods=["GET", "POST"])
def ranking():
    arquivo = "ranking.csv"
    cabecalho = ["id", "id_conteudo", "id_aluno", "pontuacao", "data_registro"]
    arquivo_alunos = "alunos.csv"
    arquivo_conteudos = "conteudos.csv"
    
    alunos = ler_csv(arquivo_alunos)
    conteudos = ler_csv(arquivo_conteudos)

    if request.method == "POST":
        dados = {
            "id": str(len(ler_csv(arquivo)) + 1),
            "id_conteudo": request.form["id_conteudo"],
            "id_aluno": request.form["id_aluno"],
            "pontuacao": request.form["pontuacao"],
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/ranking")
    
    rankings = ler_csv(arquivo)
    
    for ranking in rankings:
        aluno_nome= ""
        conteudo_nome= ""
        for aluno in alunos:
            if aluno["id"] == ranking["id_aluno"]:
                aluno_nome = aluno["nome"]
                break
        ranking["aluno_nome"] = aluno_nome if aluno_nome else "Aluno não encontrado"
        for conteudo in conteudos:
            if conteudo["id"] == ranking["id_conteudo"]:
                conteudo_nome = conteudo["titulo"]
                break
        ranking["conteudo_nome"] = conteudo_nome if conteudo_nome else "Conteúdo não encontrado"

    registros = ler_csv(arquivo)
    return render_template("ranking.html", registros=registros, alunos=alunos, conteudos=conteudos)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from routes.alunos_routes import alunos_bp
from routes.cursos_routes import cursos_bp
from routes.disciplinas_routes import disciplinas_bp
from routes.conteudos_routes import conteudos_bp
from routes.ranking_routes import ranking_bp

app = Flask(__name__)

app.register_blueprint(alunos_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(disciplinas_bp)
app.register_blueprint(conteudos_bp)
app.register_blueprint(ranking_bp)

if __name__ == "__main__":
    app.run(debug=True)

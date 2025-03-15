from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://db_lucas:1234@localhost/desenv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Mapeando tabelas (Entidades)
class Usuario(db.Model):
    __tablename__ = 'USUARIO'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Comentario(db.Model):
    __tablename__ = 'COMENTARIO'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)

@app.route('/usuarios', methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    usuario_json =  [{"id": usuario.id, "nome": usuario.nome, "email": usuario.email} for usuario in usuarios]
    return jsonify(usuario_json)

@app.route("/comentarios", methods=["GET"])
def listar_comentarios():
    comentarios = Comentario.query.all()
    comentarios_json = [
        {
            "id": comentario.id,
            "titulo": comentario.titulo,
            "descricao": comentario.descricao,
            "usuario_id": comentario.id_usuario
        } for comentario in comentarios
    ]
    return jsonify(comentarios_json)

if __name__ == "__main__":
    app.run(debug=True)
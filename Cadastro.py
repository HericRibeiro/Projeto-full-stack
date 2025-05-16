import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import Blueprint, Flask, jsonify, request, redirect, url_for, render_template

verificacoes_bp = Blueprint('verificacoes', __name__, template_folder='templates')

app = Flask(__name__)
CORS(app)


@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect('C:/Users/hericribeiro/E-commerce/database/ecommerce.db')
    cursor = conn.cursor()

    # Recebe os dados de cadastro do usuário
    dados = request.get_json()

    # Obtendo os dados do formulário
    nome = dados.get('nome')
    idade = dados.get('idade')
    email = dados.get('email')
    senha = dados.get('senha')
   
    # Verificando se o e-mail já está cadastrado
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        return jsonify({'status': 'error', 'message': 'E-mail já cadastrado.'}), 400
    else:
        # Inserindo o novo usuário no banco de dados
        cursor.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)", (nome, idade, email, senha))
        conn.commit()
        
        return jsonify({"status": "success", "redirect_to": "http://127.0.0.1:5000/home"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
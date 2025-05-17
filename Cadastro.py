import sqlite3
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import Blueprint, Flask, jsonify, request, redirect, url_for, render_template

cadastro_bp = Blueprint('cadastro', __name__)

app = Flask(__name__)
CORS(app)
load_dotenv()

banco_dados = os.getenv('BANCO_DADOS')

@cadastro_bp.route('/cadastro', methods=['POST'])
def cadastro():
    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect(banco_dados)
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
        
        return jsonify({"status": "success", "redirect_to": "https://projeto-full-stack-d2gi.onrender.com/home"}), 201

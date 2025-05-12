import requests
import pandas as pd
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_cors import CORS
import sqlite3
from flask import Flask, request, jsonify
import random

# Aplicação Flask
app = Flask(__name__)  
CORS(app)

# Função para consultar o banco de dados (arquivo Excel)
def consultar_banco(email, senha):
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect('C:/Users/hericribeiro/E-commerce/database/ecommerce.db')
    cursor = conn.cursor()

    # Consulta os dados na tabela 'usuarios' onde o email e a senha correspondem aos parâmetros
    query = "SELECT * FROM users WHERE email = ? AND senha = ?"
    cursor.execute(query, (email, senha))

    resultado = cursor.fetchone() 

    # Verifica se o resultado está vazio ou não
    if resultado:
        return True
    else:
        return False

# Rota da API para verificar os dados (será chamada com o método POST)
@app.route('/verificar_dados', methods=['POST'])
def verificar_dados():
    # Recebe os dados no formato JSON do corpo da requisição
    dados = request.get_json()
    
    # Obtém o valor do campo 'email' e 'senha' do JSON enviado
    email = dados.get('email')
    senha = dados.get('senha')

    # Verifica se o email foi informado na requisição
    if email is None:
        return jsonify({"status": "error", "message": "email ou senha não informado"}), 400

    if consultar_banco(email, senha):
        return jsonify({"status": "success", "redirect_to": "http://127.0.0.1:5000/home"}), 200
    else:
        return jsonify({"status": "error", "message": "email não encontrado"}), 404

@app.route('/cadastro', methods=['POST'])
def cadastro():
    # Conexão com o banco de dados SQLite
    conn = sqlite3.connect('C:/Users/hericribeiro/E-commerce/database/ecommerce.db')
    cursor = conn.cursor()

    # Recebe os dados de cadastro do usuário
    dados = request.get_json()

    # Obtendo os dados do formulário
    nome = dados.get('nome')
    email = dados.get('email')
    idade = dados.get('idade')
    senha = dados.get('senha')
   
    # Verificando se o e-mail já está cadastrado
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        return jsonify({'status': 'error', 'message': 'E-mail já cadastrado.'}), 400

    # Inserindo o novo usuário no banco de dados
    cursor.execute("INSERT INTO users (nome, email, idade, senha) VALUES (?, ?, ?, ?)", (nome, email, idade, senha))
    conn.commit()
    
    return jsonify({"status": "success", "redirect_to": "http://127.0.0.1:5000/home"}), 200


# Rota para a página 'home', que será renderizada quando o redirecionamento ocorrer
@app.route('/home')
def home():
    # Retorna o template 'home.html' para ser exibido ao usuário
    return render_template("home.html")


# Frase motivacional
frases_motivacionais = [
    "Acredite em você e em todo o seu potencial. Você é capaz de coisas incríveis.",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
    "Não espere por oportunidades, crie-as.",
    "A jornada pode ser longa, mas cada passo te aproxima do seu destino.",
    "Desistir não é uma opção para quem nasceu pra vencer.",
    "A persistência é o caminho do êxito.",
    "Você é mais forte do que imagina. Continue.",
    "Grandes conquistas exigem grandes esforços. Continue lutando.",
    "A coragem não é ausência de medo, é a decisão de seguir apesar dele.",
    "Você está exatamente onde precisa estar para começar algo novo."
]

@app.route('/motivacional', methods=['GET'])
def get_frases():
    # Retorna 3 frases aleatórias por chamada
    frases_aleatorias = random.sample(frases_motivacionais, 1)
    return jsonify({"frases": frases_aleatorias})

# Inicia o servidor Flask na porta 5000 com o modo de depuração ativado
if __name__ == '__main__':
    app.run(debug=True, port=5000)
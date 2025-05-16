# novo_arquivo.py
from flask import Flask
from flask_cors import CORS
from Verificação import verificacoes_bp
from Cadastro import cadastro_bp

app = Flask(__name__)
CORS(app)

# Registro dos Blueprints
app.register_blueprint(verificacoes_bp)
app.register_blueprint(cadastro_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

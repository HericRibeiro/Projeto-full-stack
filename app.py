import os
from flask import Flask
from flask_cors import CORS
from Verificação import verificacoes_bp
from Cadastro import cadastro_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(verificacoes_bp)
app.register_blueprint(cadastro_bp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

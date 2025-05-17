import os
from flask import Flask
from flask_cors import CORS
from Verificação import verificacoes_bp
from Cadastro import cadastro_bp
from flask import Blueprint, Flask, jsonify, request, redirect, url_for, render_template

app = Flask(__name__)
CORS(app)

app.register_blueprint(verificacoes_bp, urlprefix='/api')
app.register_blueprint(cadastro_bp, urlprefix='/api')

@app.route('/api/healthcheck')
def healthcheck():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

# Projeto Full Stack - API Flask

## Visão Geral
Este projeto é uma API RESTful construída com Flask, estruturada em Blueprints para modularidade e escalabilidade. Desenvolvida com foco em melhores práticas, segurança e facilidade de manutenção, a aplicação suporta funcionalidades de verificação e cadastro de usuários, preparada para integração com front-end e deployment em ambiente de produção.

## Tecnologias Utilizadas
- Python 3.11
- Flask 3.1
- Flask-CORS
- Gunicorn (Servidor WSGI para produção)
- GitHub (Controle de versão)
- Render.com (Deploy e hosting)

## Estrutura do Projeto
O projeto visa aprimorar a produtividade, sendo de maneira clara e objetiva!


# Aplicação principal com registro dos Blueprints
/app.py 

# Blueprint para rotas de verificação
/Verificacao.py 

# Blueprint para rotas de cadastro
/Cadastro.py 

# Dependências do projeto
/requirements.txt 
/README.md # Documentação do projeto


# Como Executar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/HericRibeiro/Projeto-full-stack.git
cd Projeto-full-stack


# Ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python run app.py

# Próximos passos
# Implementar autenticação JWT para segurança aprimorada.
# Documentação da API com Swagger/OpenAPI.
# Testes automatizados para garantir qualidade contínua.
# Escalabilidade horizontal via containers Docker.

##################### Contato
Heric Ribeiro - Desenvolvedor de Aplicações
LinkedIn: https://www.linkedin.com/in/heric-willian-5b78722a3/ | GitHub: https://github.com/HericRibeiro
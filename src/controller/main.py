# main.py
from flask import Flask, request, jsonify, render_template_string
from src.model.modelo import ModeloTarefa
from src.view.visao import HTML_TEMPLATE

app = Flask(__name__)
modelo = ModeloTarefa()

# Dados iniciais
if not modelo.obter_tarefas():
    modelo.cadastrar_tarefa("Estudar Padrão MVC", "Revisar separação de responsabilidades")
    modelo.cadastrar_tarefa("Configurar MkDocs", "Publicar documentação no GitHub Pages")
    modelo.cadastrar_tarefa("Deploy no Render", "Configurar Gunicorn e API Flask")

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/tarefas', methods=['GET'])
def listar():
    return jsonify(modelo.obter_tarefas())

@app.route('/tarefas', methods=['POST'])
def adicionar():
    dados = request.json
    if not dados:
        return jsonify({"erro": "Corpo da requisição vazio"}), 400
    
    modelo.cadastrar_tarefa(dados.get('descricao'), dados.get('lembrete'))
    return jsonify({"mensagem": "Tarefa cadastrada!"}), 201

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def remover(id):
    if modelo.remover_tarefa(id):
        return jsonify({"mensagem": f"Tarefa {id} removida!"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run()
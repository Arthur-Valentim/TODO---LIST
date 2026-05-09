from flask import Flask, request, jsonify
from app.modelo import ModeloTarefa

app = Flask(__name__)
modelo = ModeloTarefa()

@app.route('/tarefas', methods=['GET'])
def listar():
    return jsonify(modelo.obter_tarefas())

@app.route('/tarefas', methods=['POST'])
def adicionar():
    dados = request.json
    modelo.cadastrar_tarefa(dados.get('descricao'), dados.get('lembrete'))
    return jsonify({"mensagem": "Tarefa cadastrada!"}), 201

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def remover(id):
    if modelo.remover_tarefa(id):
        return jsonify({"mensagem": "Removida!"})
    return jsonify({"erro": "Não encontrada"}), 404

if __name__ == "__main__":
    app.run()
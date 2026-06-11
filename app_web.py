from flask import Flask, request, jsonify, render_template_string
from app.modelo import ModeloTarefa

app = Flask(__name__)
modelo = ModeloTarefa()

# Bloco de inicialização: Garante que o professor veja dados ao abrir o link
# Isso popula o ModeloTarefa assim que o servidor liga no Render
if not modelo.obter_tarefas():
    modelo.cadastrar_tarefa("Estudar Padrão MVC", "Revisar separação de responsabilidades")
    modelo.cadastrar_tarefa("Configurar MkDocs", "Publicar documentação no GitHub Pages")
    modelo.cadastrar_tarefa("Deploy no Render", "Configurar Gunicorn e API Flask")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TODO List - Web</title>
    <style>
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --bg: #f3f4f6;
            --text: #1f2937;
            --card-bg: #ffffff;
            --danger: #ef4444;
            --danger-hover: #dc2626;
        }
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 2rem;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 100%;
            max-width: 600px;
        }
        h1 {
            text-align: center;
            color: var(--primary);
            margin-bottom: 2rem;
        }
        .card {
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }
        label {
            font-weight: 600;
        }
        input {
            padding: 0.75rem;
            border: 1px solid #d1d5db;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.2s;
        }
        input:focus {
            outline: none;
            border-color: var(--primary);
        }
        button {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.2s;
            width: 100%;
            font-weight: bold;
        }
        button:hover {
            background-color: var(--primary-hover);
        }
        .btn-danger {
            background-color: var(--danger);
            padding: 0.5rem 0.75rem;
            font-size: 0.875rem;
            width: auto;
        }
        .btn-danger:hover {
            background-color: var(--danger-hover);
        }
        .task-list {
            list-style: none;
            padding: 0;
        }
        .task-item {
            background: var(--card-bg);
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: transform 0.2s;
        }
        .task-item:hover {
            transform: translateY(-2px);
        }
        .task-content h3 {
            margin: 0 0 0.25rem 0;
            font-size: 1.125rem;
            color: var(--text);
        }
        .task-content p {
            margin: 0;
            color: #6b7280;
            font-size: 0.875rem;
        }
        .empty-state {
            text-align: center;
            color: #6b7280;
            padding: 2rem 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Minhas Tarefas</h1>
        
        <div class="card">
            <form id="task-form">
                <div class="form-group">
                    <label for="descricao">Descrição da Tarefa</label>
                    <input type="text" id="descricao" required placeholder="Ex: Estudar Padrão MVC">
                </div>
                <div class="form-group">
                    <label for="lembrete">Lembrete</label>
                    <input type="text" id="lembrete" required placeholder="Ex: Hoje às 18h">
                </div>
                <button type="submit">Adicionar Tarefa</button>
            </form>
        </div>

        <ul class="task-list" id="task-list">
            <!-- Tarefas serão inseridas aqui via JavaScript -->
        </ul>
    </div>

    <script>
        const API_URL = '/tarefas';

        async function fetchTarefas() {
            try {
                const response = await fetch(API_URL);
                const tarefas = await response.json();
                renderTarefas(tarefas);
            } catch (error) {
                console.error("Erro ao carregar tarefas:", error);
            }
        }

        function renderTarefas(tarefas) {
            const list = document.getElementById('task-list');
            list.innerHTML = '';
            
            const entries = Object.entries(tarefas);
            
            if (entries.length === 0) {
                list.innerHTML = '<p class="empty-state">Nenhuma tarefa cadastrada. Adicione uma acima!</p>';
                return;
            }

            for (const [id, tarefa] of entries) {
                const li = document.createElement('li');
                li.className = 'task-item';
                li.innerHTML = `
                    <div class="task-content">
                        <h3>${tarefa.descricao}</h3>
                        <p>Lembrete: ${tarefa.lembrete}</p>
                    </div>
                    <button class="btn-danger" onclick="removerTarefa(${id})">Remover</button>
                `;
                list.appendChild(li);
            }
        }

        document.getElementById('task-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const descricao = document.getElementById('descricao').value;
            const lembrete = document.getElementById('lembrete').value;
            
            const submitBtn = e.target.querySelector('button[type="submit"]');
            submitBtn.disabled = true;
            submitBtn.textContent = 'Adicionando...';

            try {
                await fetch(API_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ descricao, lembrete })
                });

                document.getElementById('task-form').reset();
                await fetchTarefas();
            } catch (error) {
                console.error("Erro ao adicionar tarefa:", error);
                alert("Erro ao adicionar tarefa.");
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Adicionar Tarefa';
            }
        });

        async function removerTarefa(id) {
            if (confirm('Tem certeza que deseja remover esta tarefa?')) {
                try {
                    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
                    await fetchTarefas();
                } catch (error) {
                    console.error("Erro ao remover tarefa:", error);
                    alert("Erro ao remover tarefa.");
                }
            }
        }

        // Carregar tarefas inicialmente
        fetchTarefas();
    </script>
</body>
</html>
"""

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
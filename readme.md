<div align="center">
  <h1>✅ Gerenciador de Tarefas (Todo List)</h1>
  <p><i>Projeto acadêmico completo em Python focado no padrão <b>MVC</b> e <b>Spec-Driven Development</b>.</i></p>
  
  <a href="https://todo-list-s68y.onrender.com">🖥️ Aplicação Web (Render)</a> •
  <a href="https://arthur-valentim.github.io/TODO---LIST/">📚 Documentação (MkDocs)</a>
</div>

---

## 🎯 Sobre o Projeto

Este repositório contém uma aplicação web interativa de lista de tarefas (TODO List). O objetivo principal não é apenas a ferramenta em si, mas a rigorosa aplicação de padrões de engenharia de software e metodologias modernas.

O projeto foi construído utilizando um repositório único (**Monorepo**) e documentado usando o processo do **Spec-Kit**, garantindo que as especificações não fiquem apenas no papel, mas conduzam o desenvolvimento do início ao fim.

---

## 📁 Arquitetura do Projeto

A aplicação está organizada seguindo rigorosamente o padrão **MVC (Model-View-Controller)** com seus módulos encapsulados no diretório `src/`:

```text
TODO - LIST/
├── .specify/               # Infraestrutura e Memória do Agente IA (GitHub Spec Kit)
├── src/
│   ├── model/
│   │   └── modelo.py       # Dados (CRUD em RAM)
│   ├── view/
│   │   └── visao.py        # Template HTML, CSS puro e JavaScript (Vanilla)
│   └── controller/
│       └── main.py         # Rotas REST e controle com Flask
├── specs/                  # Documentação do Spec-Kit (MkDocs)
│   ├── 001-todo-mvc/       # Especificações isoladas por feature
│   └── constitution.md     # Regras globais do projeto
├── app_web.py              # Entry-point WSGI para deploy
└── readme.md               # Este arquivo
```

---

## 🛠️ Spec-Kit (Desenvolvimento Orientado a Especificação)

Seguindo a metodologia do **Spec-Driven Development**, todas as etapas arquiteturais foram documentadas e podem ser conferidas em detalhes na [Documentação MkDocs](https://arthur-valentim.github.io/TODO---LIST/). Aqui está o resumo de como o software foi planejado e executado:

### 1. 📜 Constituição (Regras Inegociáveis)
- **MVC Estrito:** Separação absoluta entre Interface (HTML/CSS), Rotas/Controle (Flask) e Dados (Memória).
- **Abordagem Stateless (Em Memória):** Por requisito acadêmico, o uso de banco de dados persistente foi vetado para este escopo. As tarefas vivem no tempo de vida da instância do servidor.
- **Monorepo:** Código e documentação (`specs/`) respiram no mesmo ambiente.

### 2. 📝 Especificação (Spec)
**Propósito:** Um organizador de tarefas rápido e acessível via navegador.
* **Histórias de Usuário Atendidas:**
  - Cadastrar nova tarefa com descrição e data/hora (lembrete).
  - Visualizar todas as tarefas pendentes de forma limpa.
  - Excluir rapidamente as atividades já concluídas.

### 3. 🏗️ Plano Técnico (Plan)
* **Model (`src/model/modelo.py`):** Dicionários em Python encarregados do CRUD em tempo de execução.
* **View (`src/view/visao.py`):** Template dinâmico injetado com Javascript (Vanilla) moderno, trazendo uma interface responsiva baseada em CSS Grid/Flexbox sem dependências pesadas.
* **Controller (`src/controller/main.py`):** Microframework **Flask** atuando como maestro. Ele provê as rotas de API Restful e entrega a View ao cliente.

### 4. ✅ Tarefas Executadas (Tasks)
- [x] Configurar ambiente inicial e repositório (Monorepo).
- [x] Desenvolver a camada de Modelo (Model) para armazenamento em memória.
- [x] Desenvolver o template frontend responsivo (View).
- [x] Desenvolver a camada Controladora usando Flask e as rotas de API.
- [x] Produzir toda a documentação das etapas (Spec-Kit) via MkDocs.
- [x] Finalizar o `requirements.txt` e efetuar o deploy automático no Render.
- [x] Integrar a CLI oficial do **GitHub Spec Kit** (`specify-cli`), adicionando a infraestrutura `.specify/` e a Constituição na memória do agente.
- [x] Reorganizar a estrutura de diretórios em `specs/` isolando arquivos por feature (`001-todo-mvc/`), seguindo as convenções oficiais.

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
Certifique-se de possuir o **Python 3+** instalado.

### 2. Passos para Inicialização

Clone o projeto e instale as dependências contidas no `requirements.txt`:
```bash
# 1. Clone este repositório
git clone https://github.com/Arthur-Valentim/TODO---LIST.git

# 2. Acesse a pasta
cd TODO---LIST

# 3. Instale os requerimentos (Flask, MkDocs, etc)
pip install -r requirements.txt
```

### 3. Subindo o Servidor

Inicie o servidor Flask diretamente da raiz:
```bash
python app_web.py
```
> Acesse **[http://localhost:5000](http://localhost:5000)** no seu navegador para interagir com a aplicação.
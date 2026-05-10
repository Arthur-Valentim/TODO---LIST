## Gerenciador de Tarefas (Todo List) - Arquitetura MVC

Este é um projeto acadêmico completo que implementa um gerenciador de tarefas utilizando **Python** e o padrão arquitetural **MVC (Model-View-Controller)**. O projeto foi desenvolvido sob a metodologia de **Spec-Driven Development**, unindo código-fonte e documentação técnica em um monorepo profissional.

## Links do Projeto em Produção

* **API Online (Render):** [https://todo-list-s68y.onrender.com/tarefas](https://todo-list-s68y.onrender.com/tarefas)
* **Documentação (GitHub Pages):** [https://arthur-valentim.github.io/TODO---LIST/](https://arthur-valentim.github.io/TODO---LIST/)

---

## Arquitetura do Sistema (MVC)

A aplicação é dividida em três camadas principais para garantir a separação de responsabilidades:

1.  **Model (`app/modelo.py`):** Contém a lógica de negócio e o gerenciamento dos dados. É aqui que as tarefas são criadas, listadas e removidas.
2.  **View (Interface):**
    * **Terminal:** Apresentação de menus e tabelas no console.
    * **Web (JSON):** Representação dos dados formatada para consumo via API.
3.  **Controller (`app_web.py` / `main.py`):** Atua como o intermediário. Recebe as entradas do usuário (seja via teclado ou via requisição HTTP) e aciona o Model.

---

## Como Rodar o Programa

### 1. Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

### 2. Instalação
Clone o repositório e instale as dependências necessárias:
```bash
# Clone o repositório
git clone [https://github.com/Arthur-Valentim/TODO---LIST.git](https://github.com/Arthur-Valentim/TODO---LIST.git)

# Entre na pasta
cd TODO---LIST

# Instale as bibliotecas (Flask e Gunicorn)
pip install -r requirements.txt
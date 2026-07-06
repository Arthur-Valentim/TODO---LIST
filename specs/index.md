# 🚀 Projeto Todo List MVC

Bem-vindo à documentação oficial do projeto **Todo List**, desenvolvida com [MkDocs](https://www.mkdocs.org/).

Esta aplicação foi rigorosamente arquitetada em **Python**, utilizando o padrão de design estrutural **MVC (Model-View-Controller)** e construída seguindo a metodologia **Spec-Driven Development (Spec-Kit)**, adotando uma estrutura de **Monorepo**.

---

## ✨ Funcionalidades Principais

*   📝 **Cadastrar Tarefas**: Permite adicionar novas atividades vinculadas a descrições claras e lembretes precisos (data e hora).
*   🗑️ **Remover Tarefas**: Exclusão ágil de itens através da interface web com feedback imediato via API.
*   ⏰ **Lembretes Dinâmicos**: Suporte integrado para anotações de tempo, ajudando o usuário a não perder prazos.
*   🌐 **Interface Web Responsiva**: Layout moderno, focado na melhor experiência de uso tanto no desktop quanto em dispositivos móveis.

---

## 🛠️ Navegando pelo Spec-Kit

Esta documentação foi elaborada para servir como o coração do projeto. Você pode acompanhar todas as fases de construção do software utilizando o menu lateral esquerdo:

1.  **[Constituição](constitution.md):** As regras inegociáveis do projeto (Por que MVC? Por que em memória?).
2.  **[Especificação (Spec)](001-todo-mvc/spec.md):** As histórias do usuário e requisitos.
3.  **[Plano Técnico (Plan)](001-todo-mvc/plan.md):** A decisão arquitetural dos componentes.
4.  **[Tarefas (Tasks)](001-todo-mvc/tasks.md):** O checklist final validando a execução.

---

## 💻 Execução Local

Para testar ou desenvolver o projeto em sua máquina, utilize o ponto de entrada principal, que inicializará o servidor web Flask.

```bash
python main.py
```

> **Dica:** O servidor estará disponível em `http://localhost:5000`.
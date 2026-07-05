# ✅ Rastreamento de Tarefas (Tasks)

O documento de tarefas valida o cumprimento dos requisitos definidos no **Plano Técnico**, servindo como um "check-point" final para garantir que a **Especificação** não ficou apenas no papel.

---

### Fase 1: Ambiente e Planejamento
- [x] Configurar o fluxo inicial de repositório (Git) consolidando a estrutura de **Monorepo**.
- [x] Redigir e formatar as documentações requeridas do Spec-Kit (Constitution, Spec, Plan, Tasks) no framework *MkDocs*.
- [x] Unificar o `readme.md` com links dinâmicos e fáceis de navegar para produção e documentação.

### Fase 2: Construção do Backend (Controller & Model)
- [x] Criar a classe Model em `app/modelo.py`, projetada para manipular dicionários no escopo de classe (armazenamento RAM).
- [x] Implementar o roteador/controlador principal `main.py` sob o Microframework Flask.
- [x] Desenvolver a API Restful nos métodos (`GET /tarefas`, `POST /tarefas`, `DELETE /tarefas/<id>`).

### Fase 3: Construção do Frontend (View)
- [x] Encapsular o esqueleto estético em `app/visao.py`.
- [x] Desenvolver o design da Interface de Usuário (UI) com variáveis em CSS Puro, evitando complexidade externa.
- [x] Integrar eventos em JavaScript para comunicação reativa via *Fetch API* junto ao Controller.

### Fase 4: Entrega (Deploy)
- [x] Mapear dependências no arquivo `requirements.txt` (`flask`, `gunicorn`, `mkdocs`).
- [x] Fornecer compatibilidade de *WSGI* (via proxy reverso/gunicorn) para ambiente de produção, caso o Render exija entrada por `app_web.py`.
- [x] Realizar o deploy do MkDocs e validar os guias online.

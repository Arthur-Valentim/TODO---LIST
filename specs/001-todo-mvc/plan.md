# 🗺️ Plano Técnico (Plan)

Este plano delineia o caminho estratégico adotado para cumprir a Especificação (Spec), definindo a infraestrutura e arquitetura técnica detalhada.

---

## 1. Topologia da Arquitetura: MVC Web

Para atender ao requisito principal, a aplicação opera estritamente no padrão **MVC (Model-View-Controller)** exposto via web.

### 🧠 Model (`src/model/modelo.py`)
- Responsabilidade: O `ModeloTarefa` é o coração dos dados.
- Implementação: Utiliza um dicionário (`dict`) em Python para prover armazenamento rápido (CRUD) **em memória**, rastreando um contador automático para gerar IDs únicos das tarefas de forma segura.

### 🖼️ View (`src/view/visao.py`)
- Responsabilidade: O componente estético entregue ao usuário. 
- Implementação: A `HTML_TEMPLATE` isolada neste arquivo provê a marcação, os estilos CSS (organizados em variáveis Root e sem dependência de frameworks externos pesados), e a reatividade JavaScript baseada na `Fetch API` assíncrona.

### 🎛️ Controller (`src/controller/main.py`)
- Responsabilidade: Intermediário central que escuta a porta de rede.
- Implementação: O servidor [Flask](https://flask.palletsprojects.com/) atua como nosso controlador web. Ele intercepta as requisições HTTP RESTful, repassa as regras para o `Model` e direciona o retorno visual adequado ou pacotes de dados JSON para a `View`.

---

## 2. Decisões Estruturais Relevantes

- **Microframework Flask:** Selecionado para permitir criação de endpoints REST sem overhead. Ideal para um escopo web direto e limpo.
- **Armazenamento Volátil:** Manter tarefas na variável de classe garante que o objetivo acadêmico de dispensar banco de dados persistente seja rigorosamente seguido.
- **Integração do Spec-Kit:** Todos os documentos do Spec-Kit são geridos através de **MkDocs**, oferecendo uma renderização estética impecável (Theme Material) a partir do mesmo repósitório (Monorepo), provendo governança absoluta da documentação.

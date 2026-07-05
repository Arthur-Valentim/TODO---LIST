# 📖 Especificação Funcional (Spec)

A Especificação é o coração criativo do projeto. Ela traduz o objetivo do negócio em requisitos técnicos explícitos. Sem uma Spec sólida, corre-se o risco de escrever códigos que os usuários não desejam.

---

## 1. Visão Geral (Propósito)
Este projeto consolida um **Gerenciador de Tarefas (TODO List)** dinâmico e focado em produtividade. A premissa básica é manter a usabilidade simples e entregar acesso direto via navegador. A meta é ajudar os usuários a organizarem suas rotinas de forma confiável.

## 2. Histórias de Usuário (User Stories)
As histórias de usuário guiam o desenvolvimento em direção às necessidades reais.

- **Cadastrar:** 
  > *"Como usuário, desejo poder inserir a descrição de uma tarefa juntamente com um lembrete (data/hora), para que eu nunca mais perca os meus compromissos."*

- **Visualizar:** 
  > *"Como usuário, desejo que, ao entrar na plataforma, eu enxergue automaticamente uma lista clara e estilizada com todos os afazeres previamente criados."*

- **Remover:** 
  > *"Como usuário, desejo um botão simples de remoção ao lado de cada tarefa, para excluir imediatamente aquilo que já finalizei ou desisti de fazer."*

---

## 3. Requisitos Não Funcionais (Limites)
- **Escalabilidade (Código):** O sistema deve ser blindado contra código macarrônico, seguindo perfeitamente o padrão **MVC**.
- **Performance de Dados:** O sistema não utilizará SGBDs (Bancos de Dados) pesados. Todo o fluxo CRUD ocorrerá na memória RAM do servidor Web, focando em alta taxa de I/O em tempo de execução.
- **Hospedagem:** O deploy final deve ser agnóstico e perfeitamente aplicável em infraestrutura gratuita de PaaS (Platform as a Service), sendo escolhido o **Render** para homologação.

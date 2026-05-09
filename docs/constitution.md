# Constituição do Projeto

Este documento apresenta as justificativas técnicas para as decisões arquiteturais tomadas no desenvolvimento desta Todo List.

## Justificativa do MVC
A escolha pelo padrão **MVC** foi feita para garantir a separação de responsabilidades. O **Modelo** gerencia os dados em memória, a **Visão** trata exclusivamente da interface com o usuário no terminal, e o **Controlador** coordena o fluxo entre ambos. Isso facilita a manutenção e futuras expansões, como a troca da interface de terminal por uma interface Web sem alterar a lógica de dados.

## Escolha de Armazenamento
Utilizamos armazenamento **em memória** (dicionários Python) para atender aos requisitos de simplicidade da especificação, eliminando a necessidade de configuração de um banco de dados persistente nesta fase acadêmica.

## Estrutura de Monorepo
O uso de um **Monorepo** permite que o código-fonte da aplicação e a documentação MkDocs coexistam no mesmo repositório, facilitando o versionamento e a sincronização entre a implementação e os manuais.
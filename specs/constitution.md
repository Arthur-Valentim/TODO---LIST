# 🏛️ Constituição do Projeto

A Constituição serve como a "lei inegociável" do projeto. Este documento define as justificativas técnicas rigorosas e as decisões arquiteturais definitivas que balizam o desenvolvimento desta Todo List, seguindo a metodologia de **Spec-Driven Development**.

---

## 1. Padrão Arquitetural: MVC
A escolha pelo padrão **MVC (Model-View-Controller)** foi adotada para garantir a total separação de responsabilidades no software:
- **Model:** Isolamento da lógica de dados. O modelo nunca deve saber como a interface web funciona.
- **View:** Isolamento da apresentação visual. Deve consumir apenas dados processados, sem implementar regras de negócio.
- **Controller:** O maestro. Garante a ponte segura entre o Model e a View.

**Justificativa:** Facilita a manutenção em longo prazo, promove a testabilidade isolada e permite futuras expansões (ex: trocar a interface HTML por React ou aplicativo mobile) sem necessidade de refatorar a base de dados ou regras de negócio.

---

## 2. Estratégia de Armazenamento
Utilizamos armazenamento estrito **em memória** por meio de estruturas nativas (dicionários em Python).

**Justificativa:** O foco desta etapa acadêmica é a estruturação arquitetural da comunicação entre camadas e a automação do fluxo com o Spec-Kit. O armazenamento em memória atende aos requisitos de simplicidade sem a sobrecarga de configurar, hospedar e orquestrar bancos de dados persistentes.

---

## 3. Gestão de Código: Monorepo
Tanto o código-fonte (backend web e frontend) quanto a documentação (MkDocs e etapas do Spec-Kit) habitam o mesmo repositório no GitHub.

**Justificativa:** O **Monorepo** garante que a documentação técnica evolua na mesma velocidade da implementação de código. Reduz a defasagem entre o que está implementado e o que está documentado, mantendo tudo centralizado e fácil de avaliar.
# app/visao.py
class VisaoTarefa:
    def mostrar_menu(self):
        print("\n--- TODO LIST ---")
        print("1. Cadastrar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas e Lembretes")
        print("4. Sair")
        return input("Escolha uma opção: ")

    def obter_dados_tarefa(self):
        descricao = input("Digite a descrição da tarefa: ")
        lembrete = input("Digite o lembrete (ex: data e hora): ")
        return descricao, lembrete

    def obter_id_remocao(self):
        try:
            return int(input("Digite o ID da tarefa a ser removida: "))
        except ValueError:
            return -1

    def mostrar_mensagem(self, mensagem):
        print(f"\nAviso: {mensagem}")

    def mostrar_tarefas(self, tarefas):
        print("\n--- Suas Tarefas ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for id_tarefa, dados in tarefas.items():
                print(f"ID: {id_tarefa} | Tarefa: {dados['descricao']} | Lembrete: {dados['lembrete']}")
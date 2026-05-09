# app/controlador.py
from app.modelo import ModeloTarefa
from app.visao import VisaoTarefa

class ControladorTarefa:
    def __init__(self):
        self.modelo = ModeloTarefa()
        self.visao = VisaoTarefa()

    def iniciar(self):
        while True:
            opcao = self.visao.mostrar_menu()
            if opcao == '1':
                descricao, lembrete = self.visao.obter_dados_tarefa()
                self.modelo.cadastrar_tarefa(descricao, lembrete)
                self.visao.mostrar_mensagem("Tarefa cadastrada com sucesso!")
            elif opcao == '2':
                id_tarefa = self.visao.obter_id_remocao()
                sucesso = self.modelo.remover_tarefa(id_tarefa)
                if sucesso:
                    self.visao.mostrar_mensagem("Tarefa removida com sucesso!")
                else:
                    self.visao.mostrar_mensagem("ID não encontrado.")
            elif opcao == '3':
                tarefas = self.modelo.obter_tarefas()
                self.visao.mostrar_tarefas(tarefas)
            elif opcao == '4':
                self.visao.mostrar_mensagem("Encerrando o programa...")
                break
            else:
                self.visao.mostrar_mensagem("Opção inválida.")
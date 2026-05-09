# app/modelo.py
class ModeloTarefa:
    def __init__(self):
        self.tarefas = {}
        self.proximo_id = 1

    def cadastrar_tarefa(self, descricao, lembrete):
        self.tarefas[self.proximo_id] = {"descricao": descricao, "lembrete": lembrete}
        self.proximo_id += 1

    def remover_tarefa(self, id_tarefa):
        if id_tarefa in self.tarefas:
            del self.tarefas[id_tarefa]
            return True
        return False

    def obter_tarefas(self):
        return self.tarefas
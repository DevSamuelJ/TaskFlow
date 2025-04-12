class ListaTarefas:
    def __init__(self):
        self.listaTarefas = []
        self.modeloTarefa = {
            "Titulo da tarefa": "",
            "Descrição da tarefa": "",
            "Prioridade da tarefa": "",
            "Ativa": None
       }
    def adicionarTarefa(self):
        self.listaTarefas.append(self.estrutura.copy())
# Não irei mais fazer com POO, irei usar somente funções, lista e dicionarios dentro de listas.
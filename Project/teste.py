def home():
    print("---TASKFLOW - GERENCIADOR DE TAREFAS---") # DEPOIS VER O MOTIVO DESSE CENTER NÃO ESTA FUNCIONANDO...
    escolha = int(input("""
    Escolha uma das opções abaixo:
     1 - Adicionar uma tarefa.
     2 - Remover uma tarefa.
     3 - Listar Tarefas.
     4 - Editar Tarafa.
     5 - Sair.
    Digite a escolha desejada:"""))
    return escolha



escolha = home() 

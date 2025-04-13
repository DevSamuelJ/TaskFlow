import time

def tarefasGerais(tituloTarefa: str, descTarefa: str, prioridadeTarefa: str):
    dicionario = {
        "Titulo da tarefa": tituloTarefa,
        "Descrição da Tarefa": descTarefa,
        "Prioridade da Tarefa": prioridadeTarefa
    }
    listaTarefas.append(dicionario)
    return listaTarefas



listaTarefas = []
contagem = 0
while True:
    print("---TASKFLOW - GERENCIADOR DE TAREFAS---".center(30)) # DEPOIS VER O MOTIVO DESSE CENTER NÃO ESTA FUNCIONANDO...
    escolha = int(input("""
    Escolha uma das opções abaixo:
     1 - Adicionar uma tarefa.
     2 - Remover uma tarefa.
     3 - Listar Tarefas.
     4 - Editar Tarafa.
     5 - Sair.
"""))

    time.sleep(0.20)
    print("Carregando.")
    time.sleep(0.25)
    print("Carregando..")
    time.sleep(0.20)
    print("Carregando...")



    if escolha == 1:
        contagem += 1
        # DEPOIS FAZER UMA FUNÇÃO SÓ DE INPUT'S PRO USUARIO!!!!
        tituloTarefa = input(f"Digite o titulo {contagem}º da tarefa: ")
        descTarefa = input(f"Digite a descrição {contagem}º da tarefa: ")
        prioridadeTarefa = input(f"Digite a prioridade {contagem}º da tarefa: ")
        print(tarefasGerais(tituloTarefa,descTarefa,prioridadeTarefa))
        continuar = input("Deseja continuar? SIM/NÃO") # ******MELHORAR O CODIGO E LOGICA A PARTIR DAQUI!******
        if continuar == "SIM":
            continue
        elif continuar == "NÃO":
            escolha = 2
        else:
            print("Escolha invalida!")


    elif escolha == 2:
        removeTarefa = input("Escreva o nome da tarefa que deseja remover: ")
        dicionario = tarefasGerais(dicionario)
        del(dicionario[removeTarefa])
        print(tarefasGerais)
import time
listaTarefas = []
def tarefasGerais(tituloTarefa: str, descTarefa: str, prioridadeTarefa: str):
    dicionario = {
        "Titulo da tarefa": tituloTarefa,
        "Descrição da Tarefa": descTarefa,
        "Prioridade da Tarefa": prioridadeTarefa
    }
    listaTarefas.append(dicionario)
    return listaTarefas

def mostrarTarefas(listaTarefas):
    contagemTarefa = 0
    for dicionario in listaTarefas:
        contagemTarefa += 1
        print(f"---Tarefa {contagemTarefa} ---")
        for chave, valor in dicionario.items():
            print(f"{chave}: {valor}")

    if escolha == 2: # TALVEZ TER FEITO ISSO NÃO TENHA SIDO UMA BOA IDEIA... VER DPS!!!
        del(dicionario[removeTarefa])
        print(f"Tarefa {removeTarefa} removida com sucesso!")



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



def loading():
    time.sleep(0.20)
    print("Carregando.")
    time.sleep(0.25)
    print("Carregando..")
    time.sleep(0.20)
    print("Carregando...")







contagem = 0
escolha = home()


while True:

    
    loading()



    if escolha == 1:
        contagem += 1
        
        tituloTarefa = input(f"Digite o titulo da {contagem}º tarefa: ")
        descTarefa = input(f"Digite a descrição da {contagem}º tarefa: ")
        prioridadeTarefa = input(f"Digite a prioridade da {contagem}º tarefa: ")
        # print(tarefasGerais(tituloTarefa,descTarefa,prioridadeTarefa))
        tarefasGerais(tituloTarefa,descTarefa,prioridadeTarefa)
        
        mostrarTarefas(listaTarefas)
        continuar = input("Deseja continuar? S/N: ").upper()# ******MELHORAR O CODIGO E LOGICA A PARTIR DAQUI!******

    elif escolha == 2: # RESOLVER OS PROBLEMAS DAQUI.
        removeTarefa = input("Escreva o nome da tarefa que deseja remover: ")
        # dicionario = tarefasGerais(tituloTarefa)

        # dicionario = tarefasGerais(dicionario)
        # del(dicionario[removeTarefa])
        # print(tarefasGerais())
        mostrarTarefas(listaTarefas)
        
    if continuar == "S":
        print("Certo... Indo pra proxima tarefa!")
    elif continuar == "N":
        print("Voltando pro menu inicial...")
        escolha = home() 
        continue
    else:
        print("Escolha invalida!")

        



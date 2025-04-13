lista = [{
    "Titulo": "titulo de teste",
    "Descrição": "Descrição de teste"
}, {
    "Titulo2": "titulo de teste2",
    "Descrição2": "Descrição de teste2"
} ]
for dicionario in lista:
    for chave, valor in dicionario.items():
        print(chave,valor)
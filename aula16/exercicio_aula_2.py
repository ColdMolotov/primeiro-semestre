dados = {"F": [0, 0], "M": [0, 0]}

with open("idades.txt", "r") as arquivo_idades:
    for linha in arquivo_idades.readlines():
        partes = linha.split(",")
        genero = partes[-1].strip()
        idade = int(partes[0])
        dados[genero][0] += 1
        dados[genero][1] += idade

media_idade_masculino = dados["M"][1] / dados["M"][0]
media_idade_feminino = dados["F"][1] / dados["F"][0]

print("Idade média dos homens: ", media_idade_masculino)
print("Idade média das mulheres: ", media_idade_feminino)

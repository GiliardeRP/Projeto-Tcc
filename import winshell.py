import winshell

while True:
    nome = input("Digite o nome do programa ou pasta que deseja abrir: ")
    atalhos = winshell.search(nome + "*", strict=False)
    if atalhos:
        for atalho in atalhos:
            atalho.Invoke()
        break
    else:
        print("O programa ou pasta não foi encontrado.")

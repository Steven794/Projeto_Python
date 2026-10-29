import os
os.system('cls')

from datetime import datetime


arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")

#OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza

nomes = []




while True:
    usuario = input(f"Você é um Estudante, Professor ou Administrador? ").lower
    if usuario == "estudante":
        print("fazer algo daqui")
    elif usuario == "professor":
        print("pedir senha e fazer algo daqui")
    elif usuario == "administrador":
        print("pedir senha e mudar tudo que ta embaixa para dentro daqui")

#OBS Omar:pessoal tudo que ta aqui membaixo deve ficar dentro desses if's de usuarios, cada usuario vai ter uma interação diferente de acordo com seu nivel de Aura


    print("Digite 1 caso deseje adicionar.\nDigite 2 para ver os dados informados. \nDigite 3 caso deseje editar um dado.\nDigite 4 para deletar algum dado.\nDigite 5 para encerrar o programa. ")
    opcao = int(input("Digite a opção que você deseja acessar: "))
    if opcao == 1:
        nome = input("Digite o nome: ")
        nomes.append(nome)
    elif opcao == 2:
        print("lista nomes: ")
        for i in range(len(nomes)):
            print(f"{i} - {nomes[i]}")

    elif opcao == 3:
        indice = int(input("Digite o índice do nome que deseja atualizar: "))
        if 0 <= indice < len(nomes):
            novo_nome = input("Digite o novo nome: ")
            nomes[indice] = novo_nome

        else:
            print("Índice Inválidos! ")

    elif opcao == 4:
        indice = int(input("Digite o índice do nome que deseja deletar: "))
        if 0 <= indice < len(nomes):
            nomes.pop(indice)

        else:
            print("Índice Inválidos! ")

    elif opcao == 5:
        print("Encerrando...")
        break

    else:
        print("Índice Inválidos! ")

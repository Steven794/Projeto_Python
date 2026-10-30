from datetime import datetime
import os
os.system('cls')


arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhas = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
administradores = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza

nomes = []

# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
# OBS omar: to tentando da uma entendida melhor no projeto no que passaram no slide, e acho que a gente é livre pra escolher algumas coisas, além do nome, matricula... a gente podia adicionar pro professor colocar uma nota para tal aluno

while True:
    print("Digite 0 caso deseje criar uma conta (Apenas Administradores podem criar contas). \nDigite 1 caso deseje logar com sua conta")
    OpcaoConta = input("Resposta: ")
    if OpcaoConta == "0":
        print("Caso tenha selecionado a opção errada: Escreva 0 para voltar ao ínicio. \nSe não, Digite 1 para continuar")
        opcaocertaouerrada = int(input("Resposta: "))
        if opcaocertaouerrada == 0:
            break
        elif opcaocertaouerrada == 1:
            print("Antes de criar uma conta, diga seu usuário e senha de administrador: ")
            usuarioADM = input("Usuário: ")
            senhaADM = input("Senha: ")
            if administradores.readline() == "usuarioADM" + " " + "senhaADM":

                print("Certo você acertou a senha.")

                niveldepermissao = input("Você é um estudante")
                usuario = input("Digite o nome do úsuario a ser criado: ")
                senha = input(
                    "Digite sua senha, ela tem que ter 8 caractéres: ")
                # OBS de OMAR: arquivo txt não aceita inteiro so string por isso a senha ta string
                if len(senha) == 8:
                    pass  # OBS de OMAR: arquivo txt não aceita inteiro so string por isso a senha ta string
            else:
                print("Você errou o úsuario ou a senha, tente novamente")

        else:
            print("Você digitou uma opção inválida")
    else:
        print("calma que to terminando essa parte")


while True:
    usuario = input(f"Você é um Estudante, Professor ou Administrador? ").lower
    if usuario == "estudante":
        print("fazer algo daqui")
    elif usuario == "professor":
        print("pedir senha e fazer algo daqui")
    elif usuario == "administrador":
        print("pedir senha e mudar tudo que ta embaixa para dentro daqui")

# OBS Omar:pessoal tudo que ta aqui membaixo deve ficar dentro desses if's de usuarios, cada usuario vai ter uma interação diferente de acordo com seu nivel de Aura
# OBS Omar: IMPORTANTE quando a gente for criar o sistema de segurança a gente NÃO pode colocar a senha no código (tenho 99% de certeza)

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

arquivo.close()
senhas.close()
administradores.close()

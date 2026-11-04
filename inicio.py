from datetime import datetime
from funcoes import *
import time  # Obs: Perguntar a Carol se pode usar!!!!!!
import random

clear_terminal()

arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhasar = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza
tentativadelogin = 0
nomes = []
matriculas = []
perfis = []
senhas = []
nome = " "
perfil = " "

# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
# OBS omar: to tentando da uma entendida melhor no projeto no que passaram no slide, e acho que a gente é livre pra escolher algumas coisas, além do nome, matricula... a gente podia adicionar pro professor colocar uma nota para tal aluno

while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input(" Se você é um Estudante digite [1]\n Professor digite [2]\n Administrador digite [3] \n Para encerrar o programa digite [4]"))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
#    if usuario == 1:
#        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
#        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
#        logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar)
    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
        professorSenhaLogar = input("Digite a senha do professor: ").strip()
#    elif usuario == 2:
#        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
#        professorSenhaLogar = input("Digite a senha do professor: ").strip()
#        logarNormal(usuario, professorUsuarioLogar=professorUsuarioLogar, professorSenhaLogar=professorSenhaLogar)
    elif usuario == 3:  # Gustavo:Aqui coloquei se a confirmação_adm for falsa, acesso negado, se nao acesso ao menu administrativo
        if not confirmacao_adm():
            print()
        else:
            while True:
                print("Bem vindo ao menu administrativo!")
                print("Digite [1] caso deseje adicionar.\nDigite [2] para ver os dados informados.\nDigite [3] caso deseje editar um dado.\nDigite [4] para deletar os dados.\nDigite [5] para encerrar o programa. ")
                opcao = int(input("Digite a opção que você deseja acessar: "))

                if opcao == 1:
                    adcionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas)

                elif opcao == 2:
                    print("===Usuários cadastrados===")

                    for i in range(len(nomes)):
                        print(f"Nome: {nomes[i]}")
                        # OBS omar: pessoal faltou ajeitar aqui pra aparecer so uma parte da matricula
                        print(f"Matrícula: {matriculas[i]}")
                        print(f"Perfil: {perfis[i]}")
                        print("hora: xx horas até yy horas")

            # Lucas: tem que mudar isso aqui porque pensa comigo vai ser um programa para muitas pessoas usar, -
            # como a pessoa X vai saber o indice do nome e da matricula dela?? nao faz sentido

            # tem que ter alguma forma de linkar a conta com seus dados ja no login da pesssoa, pegando-
            # diretamente da lista de nomes e matriculas, porque como eu vou saber-
            # o indice da minha matricula e do meu usuario no portal de aluno da cesar??? wtf
            # mas fiz desse jeito por enquanto
                elif opcao == 3:
                    escolher = int(input("digite 1. para editar o nome, 2. para editar a matricula ou 3. para editar os dois: "))
                    if escolher != 1 and escolher != 2 and escolher != 3:
                        print("codigo para edição invalido, tente novamente")
                    else:
                        if escolher == 1:
                            indice = int(
                                input("Digite o índice do nome que deseja atualizar: "))
                            if 0 <= indice < len(nomes):
                                novo_nome = input("Digite o novo nome: ")
                                nomes[indice] = novo_nome

                            else:
                                print("Índice Inválidos! ")

                        elif escolher == 2:
                            indice = int(
                                input("Digite o índice da matricula que deseja atualizar: "))
                            if 0 <= indice < len(matriculas):
                                nova_matricula = input(
                                    "Digite a nova matricula: ")
                                matriculas[indice] = nova_matricula

                            else:
                                print("Índice Inválidos! ")
                        elif escolher == 3:
                            indicenome3 = int(
                                input("Digite o índice do nome que deseja atualizar: "))
                            indicematricula3 = int(
                                input("Digite o índice da matricula que deseja atualizar: "))
                            if (0 <= indicenome3 < len(nomes)) and (0 <= indicematricula3 < len(matriculas)):
                                novo_nome3 = input("Digite o novo nome: ")
                                nomes[indicenome3] = novo_nome3
                                nova_matricula3 = input(
                                    "Digite a nova matricula: ")
                                matriculas[indicematricula3] = nova_matricula3

                            else:
                                print("Índice Inválidos! ")

                elif opcao == 4:
                    excluirUsuario(nomes, matriculas, perfis)

                elif opcao == 5:
                    for i in range(len(nomes)):
                        senhasar.write(f"\nNome: {nomes[i]} --- Matricula: {matriculas[i]} --- Perfil: {perfis[i]}")

                    print("Encerrando...")
                    break
                else:
                    print("Valor invalido!")
                    continue
    elif usuario == 4:
        break
    else:
        print("Valor inválido!")
        continue


"""    elif OpcaoConta == "1":
        print()
        print("Caso tenha selecionado a opção errada: Escreva 0 para voltar ao ínicio. \nSe não, Digite 1 para continuar")
        opcaocertaouerrada2 = int(input("Resposta: "))
        if opcaocertaouerrada2 == 0:
            break
        elif opcaocertaouerrada2 == 1:
            print("Digite seu usuário e senha. ")
            Usuario = input("Digite seu usuário: ")
            Senha = input("Digite sua senha: ")"""


# OBS Omar:pessoal tudo que ta aqui membaixo deve ficar dentro desses if's de usuarios, cada usuario vai ter uma interação diferente de acordo com seu nivel de Aura
# OBS Omar: IMPORTANTE quando a gente for criar o sistema de segurança a gente NÃO pode colocar a senha no código (tenho 99% de certeza)


arquivo.close()
senhasar.close()
confirmacao.close()
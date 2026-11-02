from datetime import datetime
from funcoes import *
import time # Obs: Perguntar a Carol se pode usar!!!!!!
from funcoes import confirmacao_adm

clear_terminal()

arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhas = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza
tentativadelogin = 0

nomes = []
matriculas = []
perfis = []

# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
# OBS omar: to tentando da uma entendida melhor no projeto no que passaram no slide, e acho que a gente é livre pra escolher algumas coisas, além do nome, matricula... a gente podia adicionar pro professor colocar uma nota para tal aluno

while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input(" Se você é um Estudante digite [1]\n Professor digite [2]\n Administrador digite [3] "))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
        logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar)

    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
        professorSenhaLogar = input("Digite a senha do professor: ").strip()
        logarNormal(usuario, professorUsuarioLogar=professorUsuarioLogar, professorSenhaLogar=professorSenhaLogar)
    elif usuario == 3:            #Gustavo:Aqui coloquei se a confirmação_adm for falsa, acesso negado, se nao acesso ao menu administrativo
        if usuario ==3:
            print("Bem vindo ao menu administrativo!")
            usuarioADM = input("Digite o nome do administrador: ").strip()
            senhaADM = input("Digite a senha do administrador: ").strip()
            confirmacao_adm(usuarioADM, senhaADM)
            print("Digite [1] caso deseje adicionar.\nDigite [2] para ver os dados informados.\nDigite [3] caso deseje editar um dado.\nDigite [4] para deletar os dados.\nDigite [5] para encerrar o programa. ")
            opcao = int(input("Digite a opção que você deseja acessar: "))

            if opcao == 1:
                nome = input("Digite o nome: ").strip()
                nomes.append(nome)

                matricula = input("Digite a matrícula: ").strip()
                matriculas.append(matricula)

                perfil = input("Digite o perfil(estudante/professor/administrador)").strip().lower()
                perfis.append(perfil)
            

            elif opcao == 2:
                print("===Usuários cadastrados===")

                for i in range(len(nomes)):
                    print(f"Nome: {nomes[i]}")
                    print(f"Matrícula: {matriculas[i]}")
                    print(f"Perfil: {perfis[i]}")
                    print("hora: xx horas até yy horas")
                    
                    #RODOLFO: A lista "perfil" não existe. Troquei o nome pra "perfis", que é o nome da lista lá encima.
                    #Lucas: tem que mudar isso aqui porque pensa comigo vai ser um programa para muitas pessoas usar, -
        #como a pessoa X vai saber o indice do nome e da matricula dela?? nao faz sentido
        
        #tem que ter alguma forma de linkar a conta com seus dados ja no login da pesssoa, pegando-
        #diretamente da lista de nomes e matriculas, porque como eu vou saber-
        #o indice da minha matricula e do meu usuario no portal de aluno da cesar??? wtf
        #mas fiz desse jeito por enquanto
            elif opcao == 3:
                escolher = int(input("digite 1. para editar o nome, 2. para editar a matricula ou 3. para editar os dois: "))
                if escolher != 1 and escolher != 2 and escolher !=3:
                    print("codigo para edição invalido, tente novamente")
                else:
                    if escolher == 1:
                        indice = int(input("Digite o índice do nome que deseja atualizar: "))
                        if 0 <= indice < len(nomes):
                            novo_nome = input("Digite o novo nome: ")
                            nomes[indice] = novo_nome
                        
                        else:
                            print("Índice Inválidos! ")

                    elif escolher == 2:
                        indice = int(input("Digite o índice da matricula que deseja atualizar: "))
                        if 0 <= indice < len(matriculas):
                            nova_matricula = input("Digite a nova matricula: ")
                            matriculas[indice] = nova_matricula
                        
                        else:
                            print("Índice Inválidos! ")
                    elif escolher == 3:
                        indicenome3 = int(input("Digite o índice do nome que deseja atualizar: "))
                        indicematricula3 = int(input("Digite o índice da matricula que deseja atualizar: "))                   
                        if (0 <= indicenome3 < len(nomes)) and (0 <= indicematricula3 < len(matriculas)):
                            novo_nome3 = input("Digite o novo nome: ")
                            nomes[indicenome3] = novo_nome3
                            nova_matricula3 = input("Digite a nova matricula: ")
                            matriculas[indicematricula3] = nova_matricula3
                        
                        else:
                            print("Índice Inválidos! ")


            elif opcao == 4:
                UsuarioSenha_juntos = []
                with open("BancoDeDados.txt", "r", encoding="utf-8") as deletar_dados:
                    for linha in deletar_dados:
                        UsuarioSenha_juntos.append(linha.strip())

                    while True:
                        print("Digite os dados para deletar os dados")
                        nome_deletar = input("Digite o do nome: ").strip()
                        senha_deletar = input("Digite a senha: ").strip()
                        juncaodedados = nome_deletar+senha_deletar

                        for linhas in UsuarioSenha_juntos:
                            if linhas == juncaodedados:
                                UsuarioSenha_juntos.remove(juncaodedados)
                                print("Dados deletados com sucesso!")
                                break

                        else:
                            print("Dados não encontrados. Por favor, reveja as informações.")
                            continue
                for i in UsuarioSenha_juntos:
                    deletar_dados.write(i)
                deletar_dados.close()

            elif opcao == 5:
                print("Encerrando...")
                break

            else:
                print("Valor invalido!")
                continue

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
senhas.close()
confirmacao.close()

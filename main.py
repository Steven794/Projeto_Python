from funcoes import *
import time  
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

while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input("Estudante digite [1]\nProfessor digite [2]\nAdministrador digite [3]\nEncerrar programa digite [4]\nDigite qual opção você deseja acessar: "))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
        maquina = input("Insira o número da máquina utilizada (entre 01-30): ")
        resultado = logarNormal(usuario,estudanteUsuarioLogar,estudanteSenhaLogar,"","")
        numero_maquina(maquina)
        print(resultado)
        if resultado == "Login de estudante permitido":
            print("Bem vindo ao menu do estudante")
            print("1.Boletim.\n2.Consultar seus dados.\n3.Consultar suas faltas.\n4.xxxxxx")

    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
        professorSenhaLogar = input("Digite a senha do professor: ").strip()
        maquina = input("Insira o número da máquina utilizada (entre 01-30): ")
        resultado = logarNormal(usuario,"","",professorUsuarioLogar,professorSenhaLogar)
        numero_maquina(maquina)
        print(resultado)

        if resultado == "Login de professor permitido":
            print("1.???????")

    elif usuario == 3:  # Gustavo:Aqui coloquei se a confirmação_adm for falsa, acesso negado, se nao acesso ao menu administrativo
        if not confirmacao_adm():
            print()
        else:
            while True:
                print("Bem vindo ao menu administrativo!")
                print("1.Adicionar usuário.\n2.Consultar dados.\n3.Editar dados.\n4.Excluir usuário.\n5.Encerrar o programa. ")
                opcao = int(input("Digite a opção que você deseja acessar: "))

                if opcao == 1:
                    adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas)

                elif opcao == 2:
                    print("=== Dados Cadastrados ===")
                    print(senhasar.read())
    
            # Lucas: tem que mudar isso aqui porque pensa comigo vai ser um programa para muitas pessoas usar, -
            # como a pessoa X vai saber o indice do nome e da matricula dela?? nao faz sentido

            # tem que ter alguma forma de linkar a conta com seus dados ja no login da pesssoa, pegando-
            # diretamente da lista de nomes e matriculas, porque como eu vou saber-
            # o indice da minha matricula e do meu usuario no portal de aluno da cesar??? wtf
            # mas fiz desse jeito por enquanto
                elif opcao == 3:
                    escolher = int(input("1.Editar nome.\n 2.Editar matrícula .\n3.Editar nome e matrícula.")) 
                    #OBS de omar: matricula tem 10 digitos e senha tem 12
                    if escolher != 1 and escolher != 2 and escolher != 3:
                        print("codigo para edição invalido, tente novamente")
                    else:
                        if escolher == 1:
                            nome = input("Digite o nome do aluno para encontrar a matricula\nObs: com letra maiuscula e minuscula ")
                            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                                linha = arquivo.readline()
                                while linha:
                                    if "matricula:" and nome in linha:
                                    # pega tudo quem vem depois de "matricula:"
                                        parte_matricula = linha.split("matricula:")[1]
                                        numero_matricula = parte_matricula.split("-").strip()
                                        print(f"matricula {numero_matricula}")
                                        break
                                    else:
                                        print("Índice Inválidos! ")

                        elif escolher == 2:
                            matricula_atualizada = []
                            matricula_antiga = input("Digite a matricula do aluno: ")
                            matricula_nova = input("Digite a nova matricula do aluno para atualizar: ")
                            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                                for linha in arquivo:
                                    if f"matrícula: {numero_matricula}" in linha:
                                        linha = linha.replace(matricula_antiga, matricula_nova)
                                    matricula_atualizada.append(linha)
                            with open("BancoDeContasExistentes.txt", "a", encoding="utf-8") as arquivo:
                                arquivo.writelines(matricula_atualizada)
                            print("Matrícula atualizada com sucesso!")
                        
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

arquivo.close()
senhasar.close()
confirmacao.close()
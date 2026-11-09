from funcoes import *
import time
import random

clear_terminal()

arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhasar = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza
# tentativadelogin = 0
nomes = []
matriculas = []
maquinas = []
perfis = []
senhas = []
nome = " "
perfil = " "
hora123 = datetime.now()
HorarioAjeitado123 = hora.strftime("%d/%m/%Y %H:%M")
tentativas123 = 5
erros123 = 0

# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação

while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input("Estudante digite [1]\nProfessor digite [2]\nAdministrador digite [3]\nEncerrar programa digite [4]\nDigite qual opção você deseja acessar: "))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
        maquina = int(input("Insira o número da máquina utilizada (entre 01-30): "))
#Mari: coloquei máquina como input para entrar no if
        resultado = logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar, "", "")

        if maquina <= 0 or maquina > 30:
            print("Opção inválida!")

        elif maquina >= 1 and maquina <= 30: 
            acessoMaquinas(usuario, "", estudanteUsuarioLogar, maquina)
            print(resultado)

            if resultado == "Login de estudante permitido":
                print("Bem vindo ao menu do estudante")
                while True:
                    print("1.Boletim.\n2.Consultar seus dados.\n3.Consultar suas faltas.\n4.Para Encerrar o seu Login.")
                    opcaoE = int(input("Digite qual opção deseja acessar: "))
                    if opcaoE == 1:
                        escolha = int(input("1. ver nota1, 2. nota2, 3. nota3, 4. mediaFinal: "))
                        mostrarNotas(escolha)
                    elif opcaoE == 2:
                        matricula_censurada = matricula_ocultada(usuario, estudanteUsuarioLogar, 2)
                        print(matricula_censurada)
                        revelar = input("Você deseja exibir a sua matrícula? ").strip().lower()
                        if revelar == "sim":
                            import random
                            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            operacao = ["+", "-", "*", "/"]
                            numero1 = random.choice(numeros)
                            numero2 = random.choice(numeros)
                            operador = random.choice(operacao)
                            pergunta = f"{numero1} {operador} {numero2}"
                            if operador == "+":
                                resultado2 = numero1 + numero2
                            elif operador == "-":
                                resultado2 = numero1 - numero2
                            elif operador == "*":
                                resultado2 = numero1 * numero2
                            elif operador == "/":
                                resultado2 = numero1 / numero2
                            print(pergunta)
                            resposta = int(input("resposta: "))
                            if resposta == resultado2:
                                print("confirmação concluida com exito")
                                matricula_sem_censura = mostrar_matricula(usuario, estudanteUsuarioLogar)
                                print(matricula_sem_censura)
                            else:
                                print("resposta incorreta")

                    elif opcaoE == 3:
                        print("Aqui ele vai consultar as faltas")

                    elif opcaoE == 4:
                        print("Encerrando Login...")
                        break
                    else:
                        print("Opção inválida")
            """if resultado == "Login não autorizado":
                tentativas123-=1
                erros123+=1

                hora_atual = datetime.now().hour#de "hora_atual" até  "print(f"Nível de risco: {risco}.")"" é a parte de análise de risco
                horario_permitido = 7<= hora_atual<=22
                risco = identificar_risco(erros123,horario_permitido)
                with open("BancoDeDados.txt","a",encoding="uft-8") as arquivo:
                    print(f"\nAluno: {usuario}")
                    print(f"\nHorário:{hora_atual}")
                    print(f"\nTentativas incorretas: {erros123}")
                    print(f"\nNível de risco: {risco}")

                print(f"Senha incorreta {tentativas123} tentativas restantes!")
                print(f"Nível de risco: {risco}.")
                                    
                if erros123 == 3:
                    arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado123}")
                    time.sleep(5)
                if erros123 == 5:
                    arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado123}")
                    time.sleep(10)"""

    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
        professorSenhaLogar = input("Digite a senha do professor: ").strip()
        maquina = int(input("Insira o número da máquina utilizada (entre 01-30): "))
        resultado = logarNormal(usuario, "", "", professorUsuarioLogar, professorSenhaLogar)

        if maquina <= 0 or maquina > 30:
            print("Opção inválida!")

        elif maquina >= 1 and maquina <= 30: 
            acessoMaquinas(usuario, "", professorUsuarioLogar, maquina)
            print(resultado)

            if resultado == "Login de professor permitido":
                while True:
                    print("Bem vindo ao menu Professor")
                    print("1.Publicar notas??.\n2.Consultar dados dos alunos.\n3.Consultar faltas dos alunos.\n4.Para Encerrar o seu Login.")
                    opcaoP = int(input("Digite um número de 1 a 4 para acessar suas opções: "))
                    if opcaoP == 1:
                        matriculaEstudante = int(input("digite os 2 primeiros digitos da matricula do aluno: "))
                        notas = int(input("1. adicionar nota 1, 2. nota2, 3. nota3: "))
                        if notas != 1 and notas != 2 and notas != 3:
                            print("codigo para adicionar notas invalido")
                        else:
                            adicionarNotas(matriculaEstudante, notas)
                      
                       
                        """adicionarNotas(matriculaEstudante, nota1, nota1add, nota2, nota2add, nota3, nota3add, mediaFinal)
                        """
      
                    elif opcaoP == 2:
                        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
                        matricula_censurada = matricula_ocultada(usuario, estudanteUsuarioLogar, 2)
                        print(matricula_censurada)

                    elif opcaoP == 3:
                        print("Aqui será possível consultar as faltas dos alunos")
                    elif opcaoP == 4:
                        print("Encerrando Login...")
                        break

                    else:
                        print("Opção inválida")
            """if resultado == "Login não autorizado":#fiz a mesma coisa do "Login não autorizado" de estudante aqui
                tentativas123-=1
                erros123+=1
                hora_atual = datetime.now().hour
                horario_permitido = 7<= hora_atual <=22

                risco = identificar_risco(erros123,horario_permitido)
                with open("BancoDeDados.txt","a",encoding="uft-8") as arquivo:
                    print(f"\nProfessor: {usuario}")
                    print(f"\nHorário:{hora_atual}")
                    print(f"\nTentativas incorretas: {erros123}")
                    print(f"\nNível de risco: {risco}")

                print(f"Senha incorreta {tentativas123} tentativas restantes!")
                print(f"Nível de risco: {risco}.")

                if erros123 == 3:
                    arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado123}")
                    time.sleep(5)
                if erros123 == 5:
                    arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado123}")
                    time.sleep(10)"""



    elif usuario == 3:  # Gustavo:Aqui coloquei se a confirmação_adm for falsa, acesso negado, se nao acesso ao menu administrativo
        if not confirmacao_adm():
            print()
        else:
            while True:
                print("Bem vindo ao menu administrativo!")
                print(
                    "1.Adicionar usuário.\n2.Consultar dados.\n3.Editar dados.\n4.Excluir usuário.\n5.Encerrar o programa. ")
                opcao = int(input("Digite a opção que você deseja acessar: "))

                if opcao == 1:
                    adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas, maquinas, maquinas)

                elif opcao == 2:
                    print("=== Dados Cadastrados ===")
                    with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as senhaler:
                        print(senhaler.read())
                    matricula_censurada = matricula_ocultada(matriculas, 2)
                    print(matricula_censurada)

            # Lucas: tem que mudar isso aqui porque pensa comigo vai ser um programa para muitas pessoas usar, -
            # como a pessoa X vai saber o indice do nome e da matricula dela?? nao faz sentido

            # tem que ter alguma forma de linkar a conta com seus dados ja no login da pesssoa, pegando-
            # diretamente da lista de nomes e matriculas, porque como eu vou saber-
            # o indice da minha matricula e do meu usuario no portal de aluno da cesar??? wtf
            # mas fiz desse jeito por enquanto
                elif opcao == 3:
                    linhas_atualizadas = []
                    encontrado = False
                    escolher = int(input("1.Editar nome.\n2.Editar matrícula.\n3.Editar nome e matrícula: "))

                    if escolher == 1:
                        nome_antigo = input("Digite o nome do aluno para atualizar\nObs: com letra maiuscula e minuscula: ")
                        nome_novo = input("Digite o novo nome do aluno\nObs: com letra maiuscula e minuscula: ")

                        with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                            for linha in arquivo:
                                if "Nome do usuário:" in linha and nome_antigo in linha:
                                    linha = linha.replace(nome_antigo, nome_novo)
                                    encontrado = True
                        
                                linhas_atualizadas.append(linha)

                        if encontrado:
                            with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                arquivo.writelines(linhas_atualizadas)
                                print(f"Nome atualizado com sucesso para: {nome_novo}")
                        else:
                            print("Usuário não encontrado no arquivo.")

                    elif escolher == 2:
                        matricula_antiga = input("Digite a matricula do aluno: ")
                        matricula_nova = input("Digite a nova matricula do aluno para atualizar: ")

                        with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                            for linha in arquivo:
                                if "matrícula:" in linha and matricula_antiga in linha:
                                    linha = linha.replace(matricula_antiga, matricula_nova)
                                    encontrado = True
                        
                        linhas_atualizadas.append(linha)

                        if encontrado:
                            with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                arquivo.writelines(linhas_atualizadas)
                                print("Matrícula atualizada com sucesso!")
                        else:
                            print("Usuário não encontrado no arquivo.")

                    elif escolher == 3:
                        matricula_antiga = input("Digite a matricula do aluno para ver se esta no sistema: ")
                        nome_antigo = input("Digite o nome do aluno para atualizar\nObs: com letra maiuscula e minuscula: ")
                        matricula_nova = input("Digite a nova matricula do aluno para atualizar: ")
                        nome_novo = input("Digite o novo nome do aluno\nObs: com letra maiuscula e minuscula: ")

                        with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                            for linha in arquivo:

                                if matricula_antiga in linha and nome_antigo in linha:
                                    linha = linha.replace(nome_antigo, nome_novo).replace(matricula_antiga, matricula_nova)
                                    encontrado = True

                                linhas_atualizadas.append(linha)

                        if encontrado:
                            with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                arquivo.writelines(linhas_atualizadas)
                            print(f"Nome atualizado com sucesso para: {nome_novo} e Matrícula atualizada para: {matricula_nova}")
                        else:
                            print("Usuário não encontrado no arquivo.")

                    else:
                        print("Digite um valor válido!")

                elif opcao == 4:
                    # excluirUsuario(nomes, matriculas, perfis)
                    # Vamo testar com o código que Omar fez e com a função acima, o que der melhor vai ser usado
                    with open("BancoDeContasExistentes.txt", "r", encoding='utf-8') as senhas123:
                        LinhaDoExcluirUsuario = int(
                            input("Informe a linha do usuário que deseja apagar: ")) - 1
                        linhas = senhas123.readlines()
                    if 0 <= LinhaDoExcluirUsuario < len(linhas):
                        del linhas[LinhaDoExcluirUsuario]

                    with open("BancoDeContasExistentes.txt", "w", encoding='utf-8') as senhas123:
                        senhas123.writelines(linhas)

                elif opcao == 5:
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
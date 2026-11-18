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
maquinas_sem_permissao = [] #Mari: essa lista vai servir como um dos parametros das maquinas banidas
nome = " "
perfil = " "
hora123 = datetime.now()
HorarioAjeitado123 = hora123.strftime("%d/%m/%Y %H:%M") 
tentativas123 = 5
erros123 = 0

# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
"""OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
string 'estudante' inteira e facilitaria apenas digitar um numero."""
while True:
        print("---Opções de login---\n\n[1] - Estudante.\n[2] - Professor.\n[3] - Administrador.\n[4] - Encerrar programa.")
        usuario = int(input("\nDigite qual opção você deseja acessar: "))
        if usuario == 1:
            clear_terminal()
            estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
            estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
            maquina = int(input("Insira o número da máquina utilizada (entre 01-30): "))
            resultado = logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar, "", "")

            #Mari: nao precisa colocar outro try porque esse no começo do programa ja vale pra toda a estrutura
            if maquina <= 0 or maquina > 30:
                print("Máquina inválida!")

            if MaquinaBloqueadaOuNao(maquina) == "Banida":
                print("Está máquina está banida!")

            elif maquina >= 1 and maquina <= 30: 
                acessoMaquinas(usuario, estudanteUsuarioLogar, "", maquina)
                print(resultado)

                if resultado == "Login de estudante permitido":
                    print("\nBem vindo ao menu do Estudante!\n")
                    while True:
                        print("---Menu do Estudante---\n\n[1] - Consultar boletim.\n[2] - Consultar seus dados.\n[3] - Consultar faltas.\n[4] - Encerrar o seu Login.")
                        opcaoE = int(input("\nDigite qual opção deseja acessar: "))
                        if opcaoE == 1:
                            #Rodolfo aqui, vamo lembrar de melhorar a exibição das notas que nem Vini disse
                            clear_terminal
                            print("1. nota 1\n2. Nota 2\n3. Nota 3\n4. Média Final")
                            escolha = int(input("Digite qual nota deseja consultar: "))
                            mostrarNotas(escolha)

                        elif opcaoE == 2:
                            #Rodolfo aqui, n podemos esquecer de deixar essa parte menos 'complicada', seguindo as dicas de Vini
                            clear_terminal()
                            matricula_censurada = matricula_ocultada(usuario, estudanteUsuarioLogar, 4)
                            print(matricula_censurada)
                            print("Deseja exibir sua matrícula?\nDigite 'S' para exibir.\nDigite 'N' para mantê-la oculta.")
                            revelar = input("Exibir matrícula? ").strip().upper()
                            
                            if revelar == "S":
                                seguranca_captcha = captcha(usuario, estudanteUsuarioLogar)
                                print(seguranca_captcha)

                            elif revelar == "N":
                                print()

                            else:
                                print("Você digitou um caracter inválido")
                        
                        elif opcaoE == 3:
                            clear_terminal()
                            mostrarFaltas(estudanteUsuarioLogar)

                        elif opcaoE == 4:
                            print("Encerrando Login...")
                            break

                        else:
                            print("Opção inválida")

                if resultado == "Login não autorizado":
                    tentativas123-=1
                    erros123+=1

                    hora_atual = datetime.now().hour #de "hora_atual" até  "print(f"Nível de risco: {risco}.")"" é a parte de análise de risco
                    horario_permitido = 7<= hora_atual<=22
                    risco = identificar_risco(erros123,horario_permitido,False)
                    
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:
                        arquivo.write(f"\nAluno: {usuario}")
                        arquivo.write(f"\nTentativas incorretas: {erros123}")
                        arquivo.write(f"\nNível de risco: {risco}")
                        arquivo.write(f"\nPerfil da tentativa: Estudante")

                    print(f"Senha incorreta {tentativas123} tentativas restantes!") 
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:                                   
                        if erros123 == 3:
                            arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado123}")
                            time.sleep(5)
                        if erros123 == 5:
                            arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado123}")
                            time.sleep(10)

        elif usuario == 2:
            clear_terminal()
            professorUsuarioLogar = input("Digite o nome do professor: ").strip()
            professorSenhaLogar = input("Digite a senha do professor: ").strip()
            maquina = int(input("Insira o número da máquina utilizada (entre 01-30): "))
            resultado = logarNormal(usuario, "", "", professorUsuarioLogar, professorSenhaLogar)

            #Mari: seria interessante colocar um try aqui mas tem que ter cuidado pra nao alterar a funcionalidade do programa
            if maquina <= 0 or maquina > 30:
                print("Opção inválida!")
            if MaquinaBloqueadaOuNao(maquina) == "Banida":
                print("Está máquina está banida!")
            
            elif maquina >= 1 and maquina <= 30: 
                acessoMaquinas(usuario, "", professorUsuarioLogar, maquina)
                print(resultado)
            
                if resultado == "Login de professor permitido":
                    print("Bem vindo ao menu Professor!\n")
                    while True:
                        print("---Menu do Professor---\n\n[1] - Publicar notas.\n[2] - Consultar dados dos alunos.\n[3] - Adicionar faltas dos alunos.\n[4] - Encerrar o seu Login.")
                        opcaoP = int(input("\nDigite qual opção deseja acessar: "))

                        if opcaoP == 1:
                            clear_terminal()
                            matriculaEstudante = int(input("Digite os 2 primeiros e 2 últimos digitos da matrícula do aluno juntos: "))
                            print("[1] - Adicionar a nota 1.\n[2] - Adicionar a nota 2.\n[3] - Adicionar a nota 3.")
                            notas = int(input("Digite qual nota deseja adicionar: "))
                            #notas = int(input("Digite [1] para adicionar a nota 1 | [2] para adicionar a nota 2 | [3] para adicionar a nota 3: "))
                            if notas != 1 and notas != 2 and notas != 3:
                                print("codigo para adicionar notas invalido")
                            else:
                                adicionarNotas(matriculaEstudante, notas)
            
                        elif opcaoP == 2:
                            clear_terminal()
                            estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
                            matricula_censurada = matricula_ocultada(usuario, estudanteUsuarioLogar, 4)
                            print(matricula_censurada)

                        elif opcaoP == 3:
                            clear_terminal()
                            matriculaEstudante = int(input("digite os 2 primeiros e 2 ultimos digitos da matricula do aluno juntos: "))
                            adicionarFaltas(matriculaEstudante)
                        
                        elif opcaoP == 4:
                            clear_terminal()
                            print("Encerrando Login...")
                            break

                        else:
                            print("Opção inválida")
                            
                if resultado == "Login não autorizado":#fiz a mesma coisa do "Login não autorizado" de estudante aqui
                    tentativas123-=1
                    erros123+=1
                    hora_atual = datetime.now().hour
                    horario_permitido = 7<= hora_atual <=22

                    risco = identificar_risco(erros123,horario_permitido,False)
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:
                        arquivo.write(f"\nProfessor: {usuario}")
                        arquivo.write(f"\nTentativas incorretas: {erros123}")
                        arquivo.write(f"\nNível de risco: {risco}")
                        arquivo.write(f"\nPerfil da tentativa: Professor")
                        if erros123 == 3:
                            arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado123}")
                            time.sleep(5)
                        if erros123 == 5:
                            arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado123}")
                            time.sleep(10)

                    print(f"Senha incorreta {tentativas123} tentativas restantes!")
                    print(f"Nível de risco: {risco}.")

        elif usuario == 3:  # Gustavo:Aqui coloquei se a confirmação_adm for falsa, acesso negado, se nao acesso ao menu administrativo
            if not confirmacao_adm():
                print()

            else:
                while True:
                    #clear_terminal()
                    print("\nBem vindo ao menu administrativo!\n")
                    #Mari: a opção de banir maquinas ainda esta em desenvolvimento
                    print("---Menu do Adminstrador---\n\n[1] - Adicionar usuário.\n[2] - Adicionar ADM\n[3] - Consultar dados/IA\n[4] - Editar dados.\n[5] - Excluir usuário.\n[6] - Banir máquinas.\n[7] - Consultar máquinas banidas.\n[8] - Encerrar sessão.")
                    opcao = int(input("\nDigite a opção que você deseja acessar: "))

                    if opcao == 1:
                        clear_terminal()
                        primeira_frase = "Cabeçário"
                        adicionarFraseContas(primeira_frase)
                        adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas, maquinas, maquinas)

                    elif opcao == 2:
                        clear_terminal()
                        criar_ADM()

                    elif opcao == 3:
                        clear_terminal()
                        escolha_nova = int(input("[1] - Dados do estudante. \n[2] - Dados do Professor. \n[3] - Acessar a IA. \n Insira uma das opções acima: "))
                        if escolha_nova == 1:
                            print("Ta sendo feito")

                        elif escolha_nova == 2:
                            print("Tambem ta sendo feito")
                            
                        elif escolha_nova == 3:
                            consultarIA()

                        print("\n=== Dados Cadastrados ===")
                        with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as senhaler:
                            print(senhaler.read())

                    elif opcao == 4:
                        clear_terminal()
                        linhas_atualizadas = []
                        encontrado = False
                        print("1.Editar nome.\n2.Editar matrícula.\n3.Editar nome e matrícula: ")
                        escolher = int(input("Digite o que você deseja editar: "))
                        #print("OBS: As matriculas tem 10 caracteres e a senha 12.")
                        '''Rodolfo: Comentei o print acima pq n acho que seja necessário manter pra o código final.
                        mas se acharem bom deixar podem colocar de volta :)'''


                        if escolher == 1:
                            clear_terminal()
                            nome_antigo = input("Digite o nome do aluno para atualizar\nObs: com letra maiuscula e minuscula\n")
                            nome_novo = input("\nDigite o novo nome do aluno\nObs: com letra maiuscula e minuscula\n")

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
                            clear_terminal()
                            matricula_antiga = input("Digite a matricula do aluno\n")
                            matricula_nova = input("Digite a nova matricula do aluno para atualizar\n")

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
                            #clear_terminal()
                            matricula_antiga = input("Digite a matricula do aluno para ver se esta no sistema: ")
                            nome_antigo = input("Digite o nome do aluno para atualizar\nObs: com letra maiuscula e minuscula\n")
                            matricula_nova = input("\nDigite a nova matricula do aluno para atualizar\n")
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

                    elif opcao == 5:
                            # excluirUsuario(nomes, matriculas, perfis)
                            # Vamo testar com o código que Omar fez e com a função acima, o que der melhor vai ser usado
                        clear_terminal()
                        with open("BancoDeContasExistentes.txt", "r", encoding='utf-8') as senhas123:
                            LinhaDoExcluirUsuario = int(
                                input("Digite a linha do arquivo que deseja apagar: \nOBS: A linha inicial é a 1. ")) - 1
                            linhas = senhas123.readlines()
                        if 0 <= LinhaDoExcluirUsuario < len(linhas):
                            del linhas[LinhaDoExcluirUsuario]

                        with open("BancoDeContasExistentes.txt", "w", encoding='utf-8') as senhas123:
                            senhas123.writelines(linhas)

                    elif opcao == 6:
                        #clear_terminal()
                        primeira_frase = "Cabeçário"
                        adicionarCabecarioBanimento(primeira_frase)
                        maquinas_banidas(maquinas_banidas)

                    elif opcao == 7:
                        #clear_terminal()
                        with open("DadosApenasADM.txt", "r", encoding="utf-8") as ArquivoDasMaquinasBanidas:
                            print(ArquivoDasMaquinasBanidas.read())


                    elif opcao == 8:
                        print("Encerrando...")
                        break

                    else:
                        print("Valor invalido!")
                        continue

        elif usuario == 4:
            print("\nEncerrando...")
            break

        else:
            print("Valor inválido!")
            continue

arquivo.close()
senhasar.close()
confirmacao.close()
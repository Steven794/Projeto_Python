from funcoes import *
import time
import random

clear_terminal()

arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhasar = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")

nomes = []
matriculas = []
maquinas = []
perfis = []
senhas = []
nome = " "
perfil = " "
hora123 = datetime.now()
HorarioAjeitado123 = hora123.strftime("%d/%m/%Y %H:%M") 
tentativas123 = 5
erros123 = 0


while True:
        primeira_frase = "cabeçalho"
        segunda_frase = "cabeçalho 2"
        terceira_frase = "cabeçalho 3"
        adicionarFraseContas(primeira_frase, segunda_frase, terceira_frase)
        
        print("---Opções de login---\n\n[1] - Estudante.\n[2] - Professor.\n[3] - Administrador.\n[4] - Encerrar programa.")
        usuario = int(input("\nDigite qual opção você deseja acessar: "))
        if usuario == 1:
            clear_terminal()
            estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
            estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
            maquina = int(input("Insira o número da máquina utilizada (entre 01-30): "))
            resultado = logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar, "", "")

            if maquina <= 0 or maquina > 30:
                print("Máquina inválida!")

            if MaquinaBloqueadaOuNao(maquina) == "Banida":
                print("Está máquina está banida!")

            elif maquina >= 1 and maquina <= 30: 
                acessoMaquinas(usuario, estudanteUsuarioLogar, "", maquina)
                print(resultado)

                if resultado == "Login de estudante permitido":
                    print("Bem vindo ao menu do Estudante!\n")
                    while True:
                        print("---Menu do Estudante---\n\n[1] - Consultar boletim.\n[2] - Consultar seus dados.\n[3] - Consultar faltas.\n[4] - Encerrar o seu Login.")
                        opcaoE = int(input("\nDigite qual opção você deseja acessar: "))
                        if opcaoE == 1:
                            clear_terminal()
                            mostrarNotas(estudanteUsuarioLogar)

                        elif opcaoE == 2:
                            clear_terminal()
                            seguranca_captcha = captcha(usuario, estudanteUsuarioLogar)
                            print(f"{seguranca_captcha}\n")
                        
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

                    hora_atual = datetime.now().hour
                    horario_permitido = 7<= hora_atual<=22
                    risco = identificar_risco(erros123,horario_permitido,False)
                    
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:
                        arquivo.write(f"\nTentativas incorretas: {erros123}")
                        arquivo.write(f"\nNível de risco: {risco}")
                        arquivo.write(f"\nPerfil da tentativa: Estudante")

                    print(f"Senha incorreta {tentativas123}, tentativas restantes!") 
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:                                   
                        if erros123 == 3:
                            arquivo.write(f"\nTentativa de login suspeita às {HorarioAjeitado123}")
                            time.sleep(5)
                        if erros123 == 5:
                            arquivo.write(f"\nTentativa de invasão às {HorarioAjeitado123}")
                            time.sleep(10)

        elif usuario == 2:
            clear_terminal()
            professorUsuarioLogar = input("Digite o nome do professor: ").strip()
            professorSenhaLogar = input("Digite a senha do professor: ").strip()
            maquina = int(input("Insira o número da máquina utilizada (entre 1-30): "))
            resultado = logarNormal(usuario, "", "", professorUsuarioLogar, professorSenhaLogar)

            if maquina <= 0 or maquina > 30:
                print("Opção inválida!")
            if MaquinaBloqueadaOuNao(maquina) == "Banida":
                print("Está máquina está banida!")
            
            elif maquina >= 1 and maquina <= 30: 
                acessoMaquinas(usuario, "", professorUsuarioLogar, maquina)
                print(resultado)
            
                if resultado == "Login de professor permitido":
                    print("Bem vindo ao Menu do Professor!\n")
                    while True:
                        print("---Menu do Professor---\n\n[1] - Publicar notas.\n[2] - Consultar dados dos alunos.\n[3] - Adicionar faltas dos alunos.\n[4] - Encerrar o seu Login.")
                        opcaoP = int(input("\nDigite qual opção você deseja acessar: "))

                        if opcaoP == 1:
                            clear_terminal()
                            matriculaEstudante = int(input("Digite os 2 primeiros e 2 últimos digitos da matrícula do aluno juntos: "))
                            print("[1] - Adicionar a nota 1.\n[2] - Adicionar a nota 2.\n[3] - Adicionar a nota 3.")
                            notas = int(input("Digite qual nota você deseja adicionar: "))
                            if notas != 1 and notas != 2 and notas != 3:
                                print("Código para adicionar notas inválido")
                            else:
                                adicionarNotas(matriculaEstudante, notas)
            
                        elif opcaoP == 2:
                            clear_terminal()
                            estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
                            matricula_censurada = matricula_ocultada(usuario, estudanteUsuarioLogar, 4)
                            print(matricula_censurada)

                        elif opcaoP == 3:
                            clear_terminal()
                            matriculaEstudante = int(input("Digite os 2 primeiros e 2 últimos digitos da matrícula do aluno juntos: "))
                            adicionarFaltas(matriculaEstudante)
                        
                        elif opcaoP == 4:
                            clear_terminal()
                            print("Encerrando Login...")
                            break

                        else:
                            print("Opção inválida!")
                            
                if resultado == "Login não autorizado":
                    tentativas123-=1
                    erros123+=1
                    hora_atual = datetime.now().hour
                    horario_permitido = 7<= hora_atual <=22

                    risco = identificar_risco(erros123,horario_permitido,False)
                    with open("BancoDeDados.txt","a",encoding="utf-8") as arquivo:
                        arquivo.write(f"\nTentativas incorretas: {erros123}")
                        arquivo.write(f"\nNível de risco: {risco}")
                        arquivo.write(f"\nPerfil da tentativa: Professor")
                        if erros123 == 3:
                            arquivo.write(f"\nTentativa de login suspeita às {HorarioAjeitado123}")
                            time.sleep(5)
                        if erros123 == 5:
                            arquivo.write(f"\nTentativa de invasão às {HorarioAjeitado123}")
                            time.sleep(10)

                    print(f"Senha incorreta {tentativas123}, tentativas restantes!")
                    print(f"Nível de risco: {risco}.")

        elif usuario == 3:
            if not confirmacao_adm():
                print()

            else:
                while True:
                    print("\nBem vindo ao Menu do Adminstrador!\n")
                    print("---Menu do Adminstrador---\n\n[1] - Adicionar usuário.\n[2] - Gerenciar contas ADM\n[3] - Consultar dados/IA\n[4] - Editar dados.\n[5] - Excluir usuário.\n[6] - Gerenciar máquinas.\n[7] - Encerrar sessão.")
                    opcao = int(input("\nDigite a opção que você deseja acessar: "))

                    if opcao == 1:
                        clear_terminal()
                        adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas, maquinas, maquinas)

                    elif opcao == 2:
                        clear_terminal()
                        print("Digite [1] adicionar conta ADM\nDigite [2] para excluir conta ADM")
                        while True:
                            opcao2 = int(input("Digite o código de acesso: "))
                            if opcao2 != 1 and opcao2 != 2:
                                print("código de escolha de conta ADM inválido!")
                                continue
                            else:
                                if opcao2 == 1:
                                    criar_ADM()
                                    break
                                else:
                                    excluirADM()
                                    break

                    elif opcao == 3:
                        clear_terminal()
                        escolha_nova = int(input("[1] - Consultar Dados \n[2] - Acessar a IA. \n Insira uma das opções acima: "))
                        if escolha_nova == 1:
                            print("\n=== Dados Cadastrados ===")
                            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as senhaler:
                                print(senhaler.read())
                            
                            
                        elif escolha_nova == 2:
                            consultarIA()

                    elif opcao == 4:
                        clear_terminal()
                        linhas_atualizadas1 = []
                        linhas_atualizadas2 = []
                        encontrado1 = False
                        encontrado2 = False

                        print("[1] - Editar nome. \n[2] - Editar matrícula.\n[3] - Editar nome e matrícula: ")
                        escolher = int(input("\nDigite a opção que você deseja editar: "))

                        if escolher == 1:
                            clear_terminal()
                            nome_antigo = input("Digite o nome para atualizar:\n")
                            nome_novo = input("\nDigite o novo nome:\n").capitalize()

                            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                                for linha in arquivo:
                                    # Corrigido para usar encontrado1 e linhas_atualizadas1
                                    if f"Nome do usuário: {nome_antigo} -" in linha:
                                        linha = linha.replace(
                                            f"Nome do usuário: {nome_antigo}",
                                            f"Nome do usuário: {nome_novo}"
                                        )
                                        encontrado1 = True
                                    linhas_atualizadas1.append(linha)

                            if encontrado1:
                                with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                    arquivo.writelines(linhas_atualizadas1)
                                print(f"Nome atualizado com sucesso para: {nome_novo}")
                            else:
                                print("Usuário não encontrado no arquivo!")

                        elif escolher == 2:
                            clear_terminal()
                            matricula_antiga = input("Digite a matrícula do aluno:\n")
                            matricula_nova = input("Digite a nova matrícula do aluno para atualizar:\n")

                            if len(matricula_antiga) != len(matricula_nova):
                                print("Erro: A nova matrícula deve ter a mesma quantidade de dígitos da antiga!")
                            else:
                                # 1. Atualiza BancoDeContasExistentes.txt
                                with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                                    for linha in arquivo:
                                        if f"Matrícula: {matricula_antiga}" in linha:
                                            linha = linha.replace(
                                                f"Matrícula: {matricula_antiga}",
                                                f"Matrícula: {matricula_nova}"
                                            )
                                            encontrado1 = True
                                        linhas_atualizadas1.append(linha)

                                # 2. Atualiza DadosDoAluno.txt (Corrigido de nome_antigo para matricula_antiga)
                                with open("DadosDoAluno.txt", "r", encoding="utf-8") as arquivo:
                                    for linha in arquivo:
                                        if f"matricula do estudante: {matricula_antiga}" in linha or f"Matricula do estudante: {matricula_antiga}" in linha:
                                            linha = linha.replace(
                                                f"matricula do estudante: {matricula_antiga}",
                                                f"matricula do estudante: {matricula_nova}"
                                            ).replace(
                                                f"Matricula do estudante: {matricula_antiga}",
                                                f"Matricula do estudante: {matricula_nova}"
                                            )
                                            encontrado2 = True
                                        linhas_atualizadas2.append(linha)

                                # Salva as alterações de forma independente
                                if encontrado1:
                                    with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(linhas_atualizadas1)
                                    print("Matrícula atualizada em BancoDeContasExistentes!")

                                if encontrado2:
                                    with open("DadosDoAluno.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(linhas_atualizadas2)
                                    print("Matrícula atualizada em DadosDoAluno!")

                                if not encontrado1 and not encontrado2:
                                    print("Usuário não encontrado em nenhum dos arquivos!")

                        elif escolher == 3:
                            clear_terminal()
                            matricula_antiga = input("Digite a matrícula antiga do aluno: ")
                            nome_antigo = input("Digite o nome antigo do aluno:\n")
                            matricula_nova = input("\nDigite a nova matrícula do aluno:\n")
                            nome_novo = input("Digite o novo nome do aluno:\n").capitalize()

                            if len(matricula_antiga) != len(matricula_nova):
                                print("Erro: A nova matrícula deve ter a mesma quantidade de dígitos da antiga!")
                            else:
                                # 1. Atualiza BancoDeContasExistentes.txt
                                with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
                                    for linha in arquivo:
                                        if f"Nome do usuário: {nome_antigo}" in linha and f"Matrícula: {matricula_antiga}" in linha:
                                            linha = linha.replace(
                                                f"Nome do usuário: {nome_antigo}",
                                                f"Nome do usuário: {nome_novo}"
                                            ).replace(
                                                f"Matrícula: {matricula_antiga}",
                                                f"Matrícula: {matricula_nova}"
                                            )
                                            encontrado1 = True
                                        linhas_atualizadas1.append(linha)

                                # 2. Atualiza DadosDoAluno.txt
                                with open("DadosDoAluno.txt", "r", encoding="utf-8") as arquivo:
                                    for linha in arquivo:
                                        if f"matricula do estudante: {matricula_antiga}" in linha or f"Matricula do estudante: {matricula_antiga}" in linha:
                                            linha = linha.replace(
                                                f"matricula do estudante: {matricula_antiga}",
                                                f"matricula do estudante: {matricula_nova}"
                                            ).replace(
                                                f"Matricula do estudante: {matricula_antiga}",
                                                f"Matricula do estudante: {matricula_nova}"
                                            )
                                            encontrado2 = True
                                        linhas_atualizadas2.append(linha)

                                if encontrado1:
                                    with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(linhas_atualizadas1)
                                    print(f"Conta atualizada: {nome_novo} - Matrícula: {matricula_nova}")

                                if encontrado2:
                                    with open("DadosDoAluno.txt", "w", encoding="utf-8") as arquivo:
                                        arquivo.writelines(linhas_atualizadas2)
                                    print("Matrícula atualizada em DadosDoAluno!")

                                if not encontrado1 and not encontrado2:
                                    print("Usuário não encontrado nos arquivos!")

                        else:
                            print("Digite um valor válido!")

                    elif opcao == 5:
                        excluirUsuario()
                        
                    elif opcao == 6:
                        print("Digite [1] para banir máquinas\nDigite [2] para desbanir máquinas\nDigite [3] para visualizar máquinas banidas")
                        while True:
                            opcao6 = int(input("Digite o código de acesso: "))
                            if opcao6 != 1 and opcao6 != 2 and opcao6 != 3:
                                print("código de escolha de máquina invalido!")
                                continue
                            else:
                                if opcao6 == 1:
                                    maquinas_banidas(maquinas_banidas)
                                    break
                                elif opcao6 == 2:
                                    desbanirMaquina()
                                    break
                                else:
                                    with open("DadosApenasADM.txt", "r", encoding="utf-8") as ArquivoDasMaquinasBanidas:
                                        print(ArquivoDasMaquinasBanidas.read())
                                        break

                    elif opcao == 7:
                        print("Encerrando...")
                        break

                    else:
                        print("Valor inválido!")
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
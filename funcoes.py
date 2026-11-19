def consultarIA():
    print("\n--- Assistente Inteligente ---")
    from agente import falar_com_agente_texto
    while True:
        pergunta = input("\nFaça sua pergunta sobre os dados (ou digite 'sair'): ").strip()
        if pergunta.lower() == "sair":
            break

        usuarios_seguros = ""
        with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arq_contas:
            for linha in arq_contas:
                partes = linha.strip().split(" - ")
                if len(partes) >= 3 and "'nome'" not in linha:
                    usuarios_seguros += f"{partes[0]} - {partes[1]} - {partes[2]}\n"

        with open("DadosDoAluno.txt", "r", encoding="utf-8") as arq_notas:
            notas_texto = arq_notas.read()

        dados_combinados = f"USUÁRIOS:\n{usuarios_seguros}\nNOTAS:\n{notas_texto}"
        falar_com_agente_texto(dados_combinados, pergunta, "Sistema Acadêmico")

from datetime import datetime
import random
import time

def clear_terminal():
    import os, platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def confirmacao_adm():
    with open("ApenasADM's.txt", "r", encoding="utf-8") as confirmacao:
        dadosCorretos = confirmacao.readlines()
        with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo:
            hora = datetime.now()
            HorarioAjeitado = hora.strftime("%d/%m/%Y %H:%M") 
            tentativas = 5
            erros = 0
        
            while tentativas > 0:
                usuarioADM = input("Informe o usuário do administrador: ").strip()
                sobrenomeADM = input("Informe o segundo nome do administrador: ").strip()
                senhaADM = input("Informe a senha do administrador: ").strip()
                ostresjuntos = f"Nome e sobrenome do ADM: {usuarioADM} {sobrenomeADM} Senha do ADM: {senhaADM}"

                if ostresjuntos in [linha.strip() for linha in dadosCorretos]:
                    print("Senha correta, login concluido.")
                    return True
            
                tentativas-=1
                erros+=1

                print(f"Senha incorreta, {tentativas} tentativas restantes!")
                if tentativas == 0:
                    time.sleep(5)

                if erros == 3:
                    arquivo.write(f"\nTentativa de login suspeita às {HorarioAjeitado} na conta de um ADM")
                    time.sleep(5)
                    
                if erros == 5:
                    arquivo.write(f"\nTentativa de invasão às {HorarioAjeitado} na conta de um ADM")
                    time.sleep(10)

            print("Acesso negado!")
            return False

#Mari: Função pra criar mais ADMs tirando a entidade original(Omar)
def criar_ADM ():
    with open("ApenasADM's.txt", "a+", encoding="utf-8") as arquivo:
        nomeADM = input("Insira o nome do ADM: ").capitalize()
        sobrenomeADM = input("Insira o sobrenome do ADM: ").capitalize()

        arquivo.seek(0)
        for linha in arquivo:
            dados = linha.strip().split()
            if not dados:
                continue

            if len(dados)>= 7  and dados[4] == "ADM:" and dados [5]== nomeADM and dados[6] == sobrenomeADM:
                print("Já existe um ADM com esse nome e sobrenome!")
                return

        senha_aleatoria_ADM = random.randint(100000000000, 999999999999)
        print(f"A sua senha é: {senha_aleatoria_ADM}")   
        arquivo.write(f"\nNome e sobrenome do ADM: {nomeADM} {sobrenomeADM} Senha do ADM: {senha_aleatoria_ADM}")

def maquinas_banidas(maquinas_barradas):
    maquinas_barradas = []
    contador_linhas = 0
    with open("DadosApenasADM.txt", "a+", encoding="utf-8") as arquivo:
        qnt_maquinas = int(input("Insira quantas máquinas serão banidas: "))
        with open("DadosApenasADM.txt", "r", encoding="utf-8") as ArquivoMaquinasBanidas:

            for i in range(qnt_maquinas):
                for linha in ArquivoMaquinasBanidas:
                    dados = linha.strip().split()
                banida = int(input("Insira um número entre 1 e 30: "))
                banidamodostring = str(banida)
                if banida < 1 or banida > 30:
                    print("Numeração inválida!")
                    continue

                else:
                    with open("DadosApenasADM.txt", "r", encoding="utf-8") as arquivo3:
                        for linha3 in arquivo3:
                            dados3 = linha3.strip().split()
                            if not dados3:
                                continue
                            if dados3[2] == "máquina":
                                banidaestringada = str(banida)
                                if dados3[4] == banidaestringada:
                                    print("Esta maquina já está banida!")
                                    break
                        else:
                            arquivo.write(f"\nNúmero da máquina banida: {banida}")
                            maquinas_barradas.append(banida)
                            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo1:
                                linhasAura = arquivo1.readlines()
                                arquivo1.close()
                                for linha1 in linhasAura:
                                    dados1 = linha1.strip().split()
                                    if not dados1:
                                        continue
                                    arquivo.seek(0)
                                    for linha2 in arquivo:
                                        dados2 = linha2.strip().split()
                                        if not dados2:
                                            continue
                                        if dados1[15] == dados2[4]:
                                            linhasAura.remove(linha1)
                                            break
                                    with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo1:
                                        arquivo1.writelines(linhasAura)

def logarNormal(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
    with open("BancoDeContasExistentes.txt", "r", encoding="utf8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if not dados:
                continue            
            if dados[0] == "Nome":
                if usuario == 1 and dados[9] == "estudante":
                    if estudanteUsuarioLogar == dados[3] and estudanteSenhaLogar == dados[12]:        
                        with open("BancoDeDados.txt", "a", encoding="utf8") as arquivo:
                            arquivo.write("\ntentativa login estudante nome digitado: " + estudanteUsuarioLogar + " " + "senha digitada: " + estudanteSenhaLogar)
                        return "Login de estudante permitido"
                elif usuario == 2 and dados[9] == "professor":
                    if professorUsuarioLogar == dados[3] and professorSenhaLogar == dados[12]:
                        with open("BancoDeDados.txt", "a", encoding="utf8") as arquivo:
                            arquivo.write("\ntentativa login professor nome digitado: " + professorUsuarioLogar + " " + "senha digitada: " + professorSenhaLogar)
                        return "Login de professor permitido"
        return "Login não autorizado"

def acessoMaquinas(usuario, nomealuno, nomeprofessor, numeracao_maquina):
    with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if usuario == 1:
            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo3:
                for linha in arquivo3:
                    dados = linha.strip().split()
                    if not dados:
                        continue
                    if dados[3] == nomealuno and dados[15] != numeracao_maquina:
                        with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo2:
                            arquivo2.write(f"\nTentativa de login suspeita do Aluno {nomealuno} na máquina {numeracao_maquina} as {data_hora}\n")
                            break
                    else:
                        arquivo.write(f"\nNome do login: {nomealuno} - Perfil: Aluno - Máquina: {numeracao_maquina}")

        elif usuario == 2:
            with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo3:
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                for linha in arquivo3:
                    dados = linha.strip().split()
                    if not dados:
                        continue
                    if dados[3] == nomeprofessor and dados[15] != numeracao_maquina:
                        with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo2:
                            arquivo2.write(f"\nTentativa de login suspeita do Professor {nomeprofessor} na máquina {numeracao_maquina} as {data_hora}\n")
                            break
                    else:
                        arquivo.write(f"\nNome do login: {nomeprofessor} - Perfil: Professor - Máquina: {numeracao_maquina}")

            print("Estrutura geral do sistema de hórario: ")
            hora = datetime.now()
            HorarioDeAcesso = hora.strftime("%H")
            acesso_normal = 0
            acesso_suspeito = 0
            login_normal = []
            login_suspeito = []
            maquinas_normais = []
            maquinas_suspeitas = []

def registrarAuditoria(operacao, usuarioAfetado):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("BancoDeContasExistentes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_hora};{operacao};{usuarioAfetado}\n")

def registrarResultado(usuario, maquina, sucesso):
    resultado = "sucesso" if sucesso else "falha"

    registrarAuditoria(f"CONSULTA_INFORMAÇÕES\nUsuário={usuario}\nMáquina={maquina}\nResultado={resultado}")

def consultarUsuario(nomes, matriculas, perfis):
    matricula = input("Digite a matrícula que deseja consultar: ").strip()
    maquina = input("Digite a máquina de origem: ").strip()

    if matricula not in matriculas:
        print("Usuário não encontrado.")
        registrarResultado(matricula, maquina, False)
        return False

    indice = matriculas.index(matricula)

    print(f"Nome: {nomes[indice]}")
    print(f"Matrícula: {matriculas[indice]}")
    print(f"Perfil: {perfis[indice]}")
    registrarResultado(matricula, maquina, True)

    print("Consulta de informações realizada com sucesso.")
    return True

def adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas, maquina, maquinas):
    senhas123 = open("BancoDeContasExistentes.txt", "a+", encoding="utf-8")
    import random
    nome = input("Digite o nome do novo usuário: ").strip().capitalize()
    matricula = random.randint(1000000000, 9999999999)

    while True:
        maquina = int(input("Insira a máquina de acesso: "))
        if maquina < 1 or maquina > 30 or maquina == "" or maquina == " ":
            print("Número de máquina inválido!")
            continue
        else:
            break

    perfil = input("Digite o perfil (estudante/professor): ").strip().lower()
    senhaAleatoria = random.randint(100000000000, 999999999999)

    if not nome or not matricula or not perfil:
        print("Preencha todos os campos!")
        return False

    if matricula in matriculas:
        print("Esse usuário já foi registrado!")
        return False

    for linha4 in senhas123:
        dados4 = linha4.strip().split()
        if not dados4:
            continue
        if dados4[15] == maquina:
            print("Essa máquina já está em uso!")
            return False
    
    arquivo5 = open("DadosApenasADM.txt", "r", encoding="utf-8")
    for linha5 in arquivo5:
        dados5 = linha5.strip().split()
        if not dados5:
            continue
        maquinaStringada = str(maquina)
        if dados5[4] == maquinaStringada:
            print("Essa máquina está banida pelo administradores!")
            return False
    arquivo5.close()
    
    perfisValidos = ("estudante", "professor")

    if perfil not in perfisValidos:
        print("Perfil inválido!")
        return False

    else:
        arquivo3 = open("BancoDeContasExistentes.txt", "r", encoding="utf-8")
        for linha in arquivo3:
            dados = linha.strip().split()
            if not dados:
                continue

            if dados[0] == "Cabeçário":
                break
                
            if dados[15] == maquina:
                return print("Não foi possível criar uma conta pois essa máquina já está em uso!")

            else:
                if perfil == "estudante":
                    nomes.append(nome)
                    matriculas.append(matricula)
                    maquinas.append(maquina)
                    perfis.append(perfil)
                    senhas.append(senhaAleatoria)

                    senhas123.write(f"\nNome do usuário: {nome} - Matrícula: {matricula} - Perfil: {perfil} - Senha: {senhaAleatoria} - Máquina: {maquina}")
                    print("Usuário adicionado com sucesso.")
                    senhas123.close()
                    print(f"Sua senha é: {senhaAleatoria}")
                    print(f"Sua matrícula é: {matricula}")

                elif perfil == "professor":
                    nomes.append(nome)
                    maquinas.append(maquina)
                    perfis.append(perfil)
                    senhas.append(senhaAleatoria)
                    print(f"Sua senha é: {senhaAleatoria}")

                    senhas123.write(f"\nNome do usuário: {nome} - ---------- ---------- - Perfil: {perfil} - Senha: {senhaAleatoria} - Máquina: {maquina}")
                    print("Usuário adicionado com sucesso.")
                    senhas123.close()
                arquivo3.close()
                return True

def excluirUsuario():
    with open("BancoDeContasExistentes.txt", "r", encoding="utf-8") as arquivo:
        listadecontas = arquivo.readlines()
    novasLinhas = []
    usuarioApagar = input("Digite o nome de usuario da conta: ")
    senhaApagar = int(input("Digite a senha associada a conta: "))
    encontrou = 0
    for linha in listadecontas:
        dados = linha.strip().split()
        if not dados:
            continue
        usuarioApagarEstringado = str(usuarioApagar)
        senhaApagarEstringada = str(senhaApagar)
        if dados[3] == usuarioApagarEstringado:
            if dados[12] == senhaApagarEstringada:
                encontrou = 1
                continue
        novasLinhas.append(linha)
    with open("BancoDeContasExistentes.txt", "w", encoding="utf-8") as arquivo1:
        arquivo1.writelines(novasLinhas)
    if encontrou == 1:
        print("Usuario excluido com sucesso!")
    else:
        print("Usuario não encontrado!")
    
def matricula_ocultada (usuario, estudanteUsuarioLogar, numeros_visiveis=4):
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue    
        if dados[0] == "Nome":
            if usuario == 1 and dados[9] == "estudante" and dados[3] == estudanteUsuarioLogar:
                stringado = dados[6]
                matriculastringada = str(stringado)

            elif usuario == 2:
                if dados[9] == "estudante" and dados[3] == estudanteUsuarioLogar:
                    stringado = dados[6]
                    matriculastringada = str(stringado)
    arquivo.close()
    estrelas = "*" * (len(matriculastringada) - numeros_visiveis)
    return f"\nA matrícula é: {matriculastringada[:2]}{estrelas}{matriculastringada[-2:]}"

def mostrar_matricula(usuario, estudanteUsuarioLogar):
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue    
        if dados[0] == "Nome":
            if usuario == 1 and dados[9] == "estudante" and dados[3] == estudanteUsuarioLogar:
                stringado = dados[6]
                matriculastringada = str(stringado)
            elif usuario == 2:
                if dados[9] == "estudante" and dados[3] == estudanteUsuarioLogar:
                    stringado = dados [6]
                    matriculastringada = str(stringado)
    arquivo.close()

    return f"A matrícula inteira é: {matriculastringada}"

def identificar_risco(tentativas, horario_permitido, maquinajabloqueada):
    if tentativas >= 5 or maquinajabloqueada:
        return "CRÍTICO"
    
    elif tentativas >= 3 or not horario_permitido:
        return "SUSPEITO"
    
    else:
        return "NORMAL"
    
def adicionarNotas(matriculaEstudante, notas):
    arquivo1 = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    nota1 = 0
    nota2 = 0
    nota3 = 0
    for linha in arquivo1:
        dados = linha.strip().split()
        if not dados:
            continue            
        if dados[0] == "Nome":
            if dados[9] == "estudante":
                if int(dados[6][:2] + dados[6][-2:]) == matriculaEstudante:
                    print("Estudante encontrado!")
                    arquivo2 = open("DadosDoAluno.txt", "r", encoding="utf8") 
                    for linha2 in arquivo2:
                        if dados[6] in linha2:
                            if notas == 1 and "nota primeira unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 1 já foi inserida!")
                            elif notas == 2 and "nota segunda unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 2 já foi inserida!")
                            elif notas == 3 and "nota terceira unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 3 já foi inserida!")  
                        
                    if notas == 1:
                        nota1add = float(input("Digite a primeira nota: "))
                        if nota1add < 0 or nota1add > 10:
                            print("Notas só podem ser entre 0 a 10")
                        else:
                            nota1 = nota1 + nota1add
                            arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                            arquivo3.write(f"\nmatricula do estudante: {dados[6]} nota primeira unidade: {nota1}")
                            arquivo3.close()
                            return print("Nota 1 adicionada com sucesso")
                    elif notas == 2:
                        arquivo7 = open("DadosDoAluno.txt", "r", encoding="utf-8")
                        nota1 = 0
                        for linha7 in arquivo7:
                            dados7 = linha7.strip().split()
                            if not dados7:
                                continue
                            if dados7[0] == "matricula":
                                if dados7[3] == dados[6]:
                                    if dados7[5] == "primeira":
                                        nota1 = 1
                        arquivo7.close()    
                        if nota1 == 0:
                                return print("É necessario adicionar a nota 1 primeiro para essa ação")
                        else:
                            nota2add = float(input("Digite a segunda nota: "))
                            if nota2add < 0 or nota2add > 10:
                                return print("Notas só podem ser entre 0 a 10")
                            else:
                                nota2 = nota2 + nota2add
                                arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                                arquivo3.write(f"\nmatricula do estudante: {dados[6]} nota segunda unidade: {nota2}")
                                arquivo3.close()
                                return print("Nota 2 adicionada com sucesso")
                    elif notas == 3:
                        arquivo7 = open("DadosDoAluno.txt", "r", encoding="utf-8")
                        nota1 = 0
                        nota2 = 0
                        for linha7 in arquivo7:
                            dados7 = linha7.strip().split()
                            if not dados7:
                                continue
                            if dados7[0] == "matricula":
                                if dados7[3] == dados[6]:
                                    if dados7[5] == "primeira":
                                        nota1 = 1
                                    elif dados7[5] == "segunda":
                                        nota2 = 1
                        arquivo7.close()
                        if nota1 == 0:
                            return print("É necessario adicionar a nota 1 primeiro para essa ação")
                        elif nota2 == 0:
                            return print("É necessario adicionar a nota 2 primeiro para essa ação")
                        else:
                            nota3add = float(input("Digite a terceira nota: "))
                            if nota3add < 0 or nota3add > 10:
                                return print("Notas só podem ser entre 0 a 10")
                            else:
                                nota3 = nota3 + nota3add
                                arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                                arquivo3.write(f"\nmatricula do estudante: {dados[6]} nota terceira unidade: {nota3}")
                                arquivo3.close()
                                nota1float = 0.0
                                nota2float = 0.0
                                nota3float = 0.0
                                arquivo4 = open("DadosDoAluno.txt", "r", encoding="utf8")
                                for linha4 in arquivo4:
                                    dados4 = linha4.strip().split()
                                    if len(dados4) >= 8:
                                        if dados4[0] == "matricula":
                                            if dados4[3] == dados[6]:
                                                if dados4[6] == "unidade:":
                                                    if dados4[5] == "primeira":
                                                        nota1float = float(dados4[7])
                                                    elif dados4[5] == "segunda":
                                                        nota2float = float(dados4[7])
                                                    elif dados4[5] == "terceira":
                                                        nota3float = float(dados4[7])
                                mediaFinal = (nota1float + nota2float + nota3float) / 3
                                arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                                arquivo3.write(f"\nmatricula do estudante: {dados[6]} media-final: {mediaFinal:.2f}")
                                arquivo4.close()
                                arquivo3.close()
                                return print("Nota 3 adicionada com sucesso, média final calculada")            
                    arquivo2.close()
    arquivo1.close()

def mostrarNotas(EstudanteUsuarioLogar):
    arquivo = open("DadosDoAluno.txt", "r", encoding="utf-8")
    print("Digite [1] para acessar nota1 \nDigite [2] para acessar nota2 \nDigite [3] para acessar nota3 \nDigite [4] para acessar media final")
    escolha = int(input("Insira um digito entre 1 e 4: "))
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue
        arquivo1 = open("BancoDeContasExistentes.txt", "r", encoding="utf-8")
        for linha1 in arquivo1:
            dados1 = linha1.strip().split()
            if not dados1:
                continue
            if dados1[3] == EstudanteUsuarioLogar:   
                if dados[3] == dados1[6]:
                    if escolha == 1 and dados[5] == "primeira":
                        print(dados[7])
                        arquivo1.close()
                        arquivo.close()
                        return
                    elif escolha == 2 and dados[5] == "segunda":
                        print(dados[7])
                        arquivo1.close()
                        arquivo.close()
                        return
                    elif escolha == 3 and dados[5] == "terceira":
                        print(dados[7])
                        arquivo1.close()
                        arquivo.close()
                        return
                    elif escolha == 4 and dados[4] == "media-final:":
                        print(dados[5])
                        arquivo1.close()
                        arquivo.close()
                        return
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:            
        return print("Código para visualização de notas inválido")
    else:
        return print("Nenhuma nota inserida")

def adicionarFaltas(matriculaEstudante):
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue                       
        if dados[0] == "Nome":
            if dados[9] == "estudante":
                if int(dados[6][:2] + dados[6][-2:]) == matriculaEstudante:
                    print("Estudante encontrado!")
                    quantidadefaltas = int(input("Insira a quantidade de faltas: "))
                    arquivo1 = open("DadosDoAluno.txt", "r", encoding="utf-8")
                    linhas = arquivo1.readlines()
                    arquivo1.close()
                    encontrou = 0
                    for i in range(len(linhas)):
                        dados1 = linhas[i].strip().split()
                        #if not dados1:
                        #    continue
                        if len(dados1) < 8:      
                            continue
                        if (dados1[3] == dados[6]) and dados1[6] == "faltas:":
                            faltaAnterior = int(dados1[7])
                            faltaAnterior = faltaAnterior + quantidadefaltas
                            faltaAnteriorStringada = str(faltaAnterior)
                            linhas[i] = f"Matricula do estudante: {dados[6]} total de faltas: {faltaAnteriorStringada}\n"
                            encontrou = 1
                            break
                    if encontrou == 1:
                        arquivo2 = open("DadosDoAluno.txt", "w", encoding="utf-8")
                        arquivo2.writelines(linhas)
                        arquivo2.close()
                    else:
                        arquivo2 = open("DadosDoAluno.txt", "a", encoding="utf-8")
                        arquivo2.write(f"\nMatricula do estudante: {dados[6]} total de faltas: {quantidadefaltas}")
                        arquivo2.close()
                    return print("Falta(s) adicionada(s) com sucesso.")                               
    arquivo.close()
            
def mostrarFaltas(estudanteUsuarioLogar):
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf-8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue
        if dados[3] == estudanteUsuarioLogar:
            arquivo1 = open("DadosDoAluno.txt", "r", encoding="utf-8")
            for linha1 in arquivo1:
                dados1 = linha1.strip().split()
                #if not dados1:
                #    continue
                if len(dados1) < 8:      
                    continue
                if (dados1[3] == dados[6]) and (dados1[6] == "faltas:"):
                    return print(f"Quantidade de faltas: {dados1[7]}") 
            else:
                return print("Não existe faltas atreladas ao seu usuário no sistema!")
    arquivo.close()
    arquivo1.close()

def captcha(usuario, estudanteUsuarioLogar):
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    operacao = ["+", "-", "*"]
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
    print(pergunta)
    
    resposta = int(input("Resposta: "))

    if resposta == resultado2:
        print("Confirmação concluída com êxito.")
        return mostrar_matricula(usuario, estudanteUsuarioLogar)

    else:
        return print("Resposta incorreta!")
    
def adicionarFraseContas(primeira_frase, segunda_frase, terceira_frase):
    arquivo = open("BancoDeContasExistentes.txt", "r+", encoding="utf-8")
    arquivo2 = open("DadosApenasADM.txt", "r+", encoding="utf-8")
    arquivo3 = open("BancoDeDados.txt", "r+", encoding="utf-8")
    arquivo4 = open("DadosDoAluno.txt", "r+", encoding="utf-8")
    primeira_frase = "Nome do usuário: 'nome' - Matrícula: 'matricula' - Perfil: 'perfil' - Senha: 'senhaAleatoria' - Máquina: 'maquina'"
    segunda_frase = "Número da máquina banida: 'máquina-banida'"
    terceira_frase = "Neste arquivo txt encontram-se os dados relacionados as tentativas de login fora do padrão considerado normal"
    quarta_frase = "Exibição das notas e faltas de todos os alunos cadastrados no sentinela.log"
    arquivo.seek(0)

    conteudo = arquivo.read()
    if primeira_frase.strip() not in conteudo:
        arquivo.write(primeira_frase)

        arquivo.close()

    conteudo_dois = arquivo2.read()
    if segunda_frase.strip() not in conteudo_dois:
        arquivo2.write(segunda_frase)

        arquivo2.close()

    conteudo_tres = arquivo3.read()
    if terceira_frase.strip() not in conteudo_tres:
        arquivo3.write(terceira_frase)

        arquivo3.close()

    conteudo_quatro = arquivo4.read()
    if quarta_frase.strip() not in conteudo_quatro:
        arquivo4.write(quarta_frase)

        arquivo4.close()

'''def MaquinaBloqueadaOuNao(maquina):
    ArquivoMaquinasBanidas = open("DadosApenasADM.txt", "r", encoding="utf-8")
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for linha in ArquivoMaquinasBanidas:
        dados = linha.strip().split()
        maquinaModoString = str(maquina)
        if maquinaModoString == dados[4]:
            print("Está máquina está banida!!")
            time.sleep(5)
            with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo67:
                arquivo67.write(f"Tentativa de login suspeita as {data_hora} pela máquina {maquina} que está banida")
            return "Banida"
    ArquivoMaquinasBanidas.close()'''

def MaquinaBloqueadaOuNao(maquina):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("DadosApenasADM.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            if not linha.startswith("Número da máquina banida:"):
                continue

            partes = linha.split(":", 1)
            numero_banido = partes[1].strip()

            if numero_banido == str(maquina):
                print("Esta máquina está banida!")

                with open("BancoDeDados.txt", "a", encoding="utf-8") as arquivo_log:
                    arquivo_log.write(f"\nTentativa de login suspeita às {data_hora} pela máquina{maquina} que está banida.\n")

                return "Banida"

    return "Não banida"
def desbanirMaquina():
    with open("DadosApenasADM.txt", "r", encoding="utf-8") as arquivo:
        listamaquina = arquivo.readlines()
    novasLinhas = []
    maquinadesban = int(input("Digite a máquina que você queria desbanir: "))
    if maquinadesban < 1 or maquinadesban > 30:
        return print("máquina invalida!")
    encontrou = 0  
    for linha in listamaquina:
        dados = linha.strip().split()
        if not dados:
            continue
        maquinadesbanEstringada = str(maquinadesban)
        if dados[4] == maquinadesbanEstringada:
            encontrou = 1
            continue
        novasLinhas.append(linha)
    with open("DadosApenasADM.txt", "w", encoding="utf-8") as arquivo1:
        arquivo1.writelines(novasLinhas)
    if encontrou == 1:
        print("máquina desbanida com sucesso!")
    else:
        print("essa máquina não estava banida!")

def excluirADM():
    with open("ApenasADM'S.txt", "r", encoding="utf-8") as arquivo:
        listaADM = arquivo.readlines()
    novasLinhas = []
    nomeADM = input("Digite o primeiro nome da conta Associada ao ADM: ")
    sobrenomeADM = input("Digite o sobrenome da conta Associada ao ADM: ")
    senhaADM = int(input("Digite a senha da conta Associada ao ADM: "))
    encontrou = 0
    for linha in listaADM:
        dados = linha.strip().split()
        if not dados:
            continue
        nomeADMEstrigado = str(nomeADM)
        sobrenomeADMEstringado = str(sobrenomeADM)
        senhaADMEstringada = str(senhaADM)
        if dados[5] == nomeADMEstrigado:
            if dados[6] == sobrenomeADMEstringado:
                if dados[10] == senhaADMEstringada:
                    encontrou = 1
                    continue
        novasLinhas.append(linha)
    with open("ApenasADM'S.txt", "w", encoding="utf-8") as arquivo1:
        arquivo1.writelines(novasLinhas)
    if encontrou == 1:
        print("Conta de ADM excluida com sucesso!")
    else:
        print("Conta de ADM não encontrada!")
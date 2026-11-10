from datetime import datetime

def clear_terminal():
    import os, platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Função que confirma se a entidade é adm
def confirmacao_adm():
    import time
    confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")
    arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
    hora = datetime.now()
    HorarioAjeitado = hora.strftime("%d/%m/%Y %H:%M")
    tentativas = 5
    erros = 0

    while tentativas > 0:
        usuarioADM = input("Informe o usuario do administrador: ").strip()
        senhaADM = input("Informe a senha do administrador: ").strip()
        #maquina = input("Insira o número da máquina utilizada (entre 01-30): ")
        osdoisjuntos = usuarioADM+senhaADM

        if osdoisjuntos == confirmacao.readline():
            print("Senha correta, login concluido.")
            return True
        
        tentativas-=1
        erros+=1
        print(f"Senha incorreta {tentativas} tentativas restantes!")
        if tentativas == 0:
            time.sleep(5)
        if erros == 3:
            arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado}")
            time.sleep(5)
            
        if erros == 5:
            arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado}")
            time.sleep(10)
    print("Acesso negado!")
    return False
    confirmacao.close()
    arquivo.close()    

def logarNormal(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue            
        if dados[0] == "Nome":
            if usuario == 1 and dados[9] == "estudante":
                if estudanteUsuarioLogar == dados[3] and estudanteSenhaLogar == dados[12]:        
                    arquivo = open("BancoDeDados.txt", "a", encoding="utf8")
                    arquivo.write("\ntentativa login estudante nome digitado: " + estudanteUsuarioLogar + " " + "senha digitada: " + estudanteSenhaLogar)
                    arquivo.close()
                    return "Login de estudante permitido"
            elif usuario == 2 and dados[9] == "professor":
                if professorUsuarioLogar == dados[3] and professorSenhaLogar == dados[12]:
                    arquivo = open("BancoDeDados.txt", "a", encoding="utf8")
                    arquivo.write("\ntentativa login professor nome digitado: " + professorUsuarioLogar + " " + "senha digitada: " + professorSenhaLogar)
                    arquivo.close()
                    return "Login de professor permitido"
    arquivo.close()
    return "Login não autorizado"

maquinas = []

#Mari: lembrando que umm usuário só pode acessar uma máquina, caso contrário deverá ser alertado ao adm que mais de um usuário acessou a maquina 
"""def numero_maquina (usuario, nomeprofessor, numeracao_maquina):
    nome_arquivo = "BancoDeContasExistentes.txt"
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    for linha in nome_arquivo:
        dados = linha.strip().split()
        if not dados:
            continue

        if dados[15] == numeracao_maquina:
            break

        else:
            if usuario == 2 and dados[9] == "professor":
                novas_linhas = []
                for linha in linhas:
                    if f"Nome do usuário: {nomeprofessor}" in linha:
                        linha = linha.strip() + f" - Máquina: {numeracao_maquina}\n"

                    novas_linhas.append(linha)

                with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                    arquivo.writelines(novas_linhas)

                maquinas.append(numeracao_maquina)"""


def acessoMaquinas(usuario, nomealuno, nomeprofessor, numeracao_maquina):
    arquivo = open("DadosApenasADM.txt", "a", encoding="utf-8")
    if usuario == 1:
        arquivo.write(f"\nNome do login: {nomealuno} - Perfil: Aluno - Máquina: {numeracao_maquina}")

    elif usuario == 2:
        arquivo3 = open("DadosApenasADM.txt", "r", encoding="utf-8")
        for linha in arquivo3:
            dados = linha.strip().split()
            if not dados:
                continue
            if dados[3] == nomeprofessor and dados[9] != numeracao_maquina:
                arquivo2 = open("BancoDeDados.txt", "a", encoding="utf-8")
                arquivo2.write(f"\nTentativa de login suspeita do Professor {nomeprofessor} na máquina {numeracao_maquina}\n")
                arquivo2.close()
                break
        else:
            arquivo.write(f"\nNome do login: {nomeprofessor} - Perfil: Professor - Máquina: {numeracao_maquina}")

        arquivo3.close()
    arquivo.close()

print("Estrutura geral do sistema de hórario: ")
hora = datetime.now()
HorarioDeAcesso = hora.strftime("%H")
acesso_normal = 0
acesso_suspeito = 0
login_normal = []
login_suspeito = []
maquinas_normais = []
maquinas_suspeitas = []

def timer(HorarioDeAcesso, tipo_usuario, conta_estudante, conta_professor, ):
    if HorarioDeAcesso >= 7 and HorarioDeAcesso <= 22:
        if tipo_usuario == 1:
            acesso_normal+=1
            login_normal.append(conta_estudante)
            maquinas_normais.append()

        elif tipo_usuario ==2:
            acesso_normal+=1
            login_normal.append(conta_estudante)
            maquinas_normais.append()

        return 
        #(OMAR): isso vai dizer que pelo menos o horário de acesso não é suspeito
    else:
        if tipo_usuario == 1:
            acesso_suspeito+=1
            login_suspeito.append(conta_professor)
            maquinas_suspeitas.append()

        elif tipo_usuario ==2:
            acesso_normal+=1
            login_suspeito.append(conta_professor)
            maquinas_suspeitas.append()
        return "Tente logar em outro horario"
        #nessa parte a gente vai ter que classificar já que a tentativa é suspeita
        
ARQUIVO_USUARIOS = "BancoDeContasExistentes.txt"
SEPARADOR = ";"

#RODOLFO: Registrar Horário de entrada
def registrarAuditoria(operacao, usuarioAfetado):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("BancoDeContasExistentes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_hora};{operacao};{usuarioAfetado}\n")

#RODOLFO: Essa função registra se teve sucesso ou falha na consulta de informações.
def registrarResultado(usuario, maquina, sucesso):
    resultado = "sucesso" if sucesso else "falha"

    registrarAuditoria(f"CONSULTA_INFORMAÇÕES\nUsuário={usuario}\nMáquina={maquina}\nResultado={resultado}")

#RODOLFO: Isso daqui é pra conferir se o usuário de fato existe, usei ela nas funções de adicionar e excluir usuário.
def salvarUsuario(nomes, matriculas, perfis):
    if not (len(nomes) == len(matriculas) == len(perfis)):
        raise ValueError("Usuário não encontrado ou incoerente com o que foi listado.")

    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:
        for nome, matricula, perfil in zip(nomes, matriculas, perfis):
            arquivo.write(
                f"{nome}{SEPARADOR}"
                f"{matricula}{SEPARADOR}"
                f"{perfil}\n")

#RODOLFO: Essa daqui é pra chamar no código principal, vai dizer se a consulta deu certo ou errado.
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

#RODOLFO: Essa função serve pra carregar os usuários de uma rodagem do código pra outra.
def carregarUsuario(nomes, matriculas, perfis, maquinas):
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(SEPARADOR)

                if len(dados) != 3:
                    continue

                nome, matricula, perfil, numeracao_maquina = dados

                nomes.append(nome)
                matriculas.append(matricula)
                perfis.append(perfil)
                maquinas.append(numeracao_maquina)

    except FileNotFoundError:
        pass

#RODOLFO: Função para adicionar novos usuários (lembrar de chamar no código principa).
def adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas, maquina, maquinas):
    senhas123 = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
    import random
    nome = input("Digite o nome do novo usuário: ").strip()
    matricula = random.randint(1000000000, 9999999999)
    maquina = input("Insira a máquina de acesso: ").strip()
    perfil = input("Digite o perfil (estudante/professor): ").strip().lower()
    senhaAleatoria = random.randint(100000000000, 999999999999)
    print(f"Sua senha é: {senhaAleatoria}")
    print(f"Sua matrícula é: {matricula}")

    if not nome or not matricula or not perfil:
        print("Preencha todos os campos!")
        return False

    if matricula in matriculas:
        print("Esse usuário já foi registrado.")
        return False

    if maquina in maquinas:
        print("Essa máquina já está em uso!")
        return False

    perfisValidos = ("estudante", "professor")

    if perfil not in perfisValidos:
        print("Perfil inválido!")
        return False

    nomes.append(nome)
    matriculas.append(matricula)
    maquinas.append(maquina)
    perfis.append(perfil)
    senhas.append(senhaAleatoria)

    salvarUsuario(nomes, matriculas, perfis)
    senhas123.write(f"\nNome do usuário: {nome} - Matrícula: {matricula} - Perfil: {perfil} - Senha: {senhaAleatoria} ")
    print("Usuário adicionado com sucesso. ")
    senhas123.close()
    return True

#RODOLFO: Função para excluir o usuário (só chamar lá no código principal agr).
def excluirUsuario(nomes, matriculas, perfis):
    matricula = input("Digite a matrícula do usuário que será exluído: ").strip()

    if matricula not in matriculas:
        print("usuário não encontrado.")
        return False

    else:
        indiceMatricula = matriculas.index(matricula)

        print(f"Nome: {nomes[indiceMatricula]}")
        print(f"Perfil: {perfis[indiceMatricula]}")

        confirmar = input("Digite 'S' para confirmar a exclusão: ").strip().upper()

        if confirmar != 'S':
            print("Exclusão cancelada.")
            return False

    nomeExcluido = nomes[indiceMatricula]

    del nomes[indiceMatricula]
    del perfis[indiceMatricula]
    del matriculas[indiceMatricula]

    salvarUsuario(nomes, matriculas, perfis)
    registrarAuditoria("EXCLUSÃO_USUARIO", f"{nomeExcluido} - matrícula {matricula}")
    print("Usuário excluído com sucesso.")
    return True

def matricula_ocultada (usuario, estudanteUsuarioLogar, numeros_visiveis=2):
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
    estrelas = "*" * (len(matriculastringada) - numeros_visiveis)
    return f"A matrícula é: {matriculastringada[:2]}{estrelas}"

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
                if int(dados[6][:2]) == matriculaEstudante:
                    print("Estudante encontrado!")
                    arquivo2 = open("DadosDoAluno.txt", "r", encoding="utf8") ###
                    for linha2 in arquivo2:
                        if dados[6] in linha2:
                            if notas == 1 and "nota primeira unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 1 ja foi inserida!")
                            elif notas == 2 and "nota segunda unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 2 ja foi inserida!")
                            elif notas == 3 and "nota terceira unidade:" in linha2:
                                arquivo2.close()
                                arquivo1.close()
                                return print("Nota 3 ja foi inserida!")  ###
                    if notas == 1:
                        nota1add = float(input("digite a primeira nota: "))
                        if nota1add < 0 or nota1add > 10:
                            print("notas so podem ser de 0 a 10")
                        else:
                            nota1 = nota1 + nota1add
                            arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                            arquivo3.write(f"\nmatricula do estudante: {dados[6]} nota primeira unidade: {nota1}")
                            arquivo3.close()
                            return print("nota1 adicioanda com sucesso")
                    elif notas == 2:
                        nota2add = float(input("digite a primeira nota: "))
                        if nota2add < 0 or nota2add > 10:
                            print("notas so podem ser de 0 a 10")
                        else:
                            nota2 = nota2 + nota2add
                            arquivo3 = open("DadosDoAluno.txt", "a", encoding="utf8")
                            arquivo3.write(f"\nmatricula do estudante: {dados[6]} nota segunda unidade: {nota2}")
                            arquivo3.close()
                            return print("nota2 adicioanda com sucesso")
                    elif notas == 3:
                        nota3add = float(input("digite a primeira nota: "))
                        if nota3add < 0 or nota3add > 10:
                            print("notas so podem ser de 0 a 10")
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
                            arquivo3.write(f"\nmatricula do estudante: {dados[6]} media-final: {mediaFinal:2f}")
                            arquivo4.close()
                            arquivo3.close()
                            return print("nota3 adicioanda com sucesso, e media final formada")
                    arquivo2.close()
    arquivo1.close()

def mostrarNotas(escolha):
    arquivo = open("DadosDoAluno.txt", "r", encoding="utf-8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue
        arquivo1 = open("BancoDeContasExistentes.txt", "r", encoding="utf-8")
        for linha1 in arquivo1:
            dados1 = linha1.strip().split()
            if not dados1:
                continue
            if len(dados1) < 7:
                continue
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
        arquivo1.close()
    arquivo.close()
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4: 
        return print("codigo para visualização de notas invalido")
    else:
        return print("nenhuma nota inserida")

def adicionarFaltas(matriculaEstudante): ############ ADICIONAR MAIS FALTAS ELE DA MAIS UM WRITE AI INVES DE SOMAR E SOBREPOR
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue            
        if dados[0] == "Nome":
            if dados[9] == "estudante":
                if int(dados[6][:2]) == matriculaEstudante:
                    print("Estudante encontrado!")
                    arquivo1 = open("DadosDoAluno.txt", "r", encoding="utf-8")
                    for linha1 in arquivo1:
                        dados1 = linha1.strip().split()
                        if not dados1:
                            continue
                        if len(dados1) != 7 and dados1[4] != "total":  ########### errado?
                            quantidadefaltas = int(input("qual a quantidade de faltas: "))
                            arquivo2 = open("DadosDoAluno.txt", "a", encoding="utf-8")
                            arquivo2.write(f"\nMatricula do estudante: {dados[6]} total de faltas: {quantidadefaltas}")
                            arquivo2.close()
                            return print("falta adicionada com sucesso")                      
                        elif dados1[3] == dados[6] and dados1[6] == "faltas": ############## nao sei???????
                            quantidadefaltas = int(input("qual a quantidade de faltas: "))
                            arquivo2 = open("DadosDoAluno.txt", "a", encoding="utf-8")
                            faltaAnterior = int(dados[7])
                            faltaAnterior = faltaAnterior + quantidadefaltas
                            faltaAnteriorStringada = str(faltaAnterior)
                            dados[7] = dados[7].replace(dados[7], faltaAnteriorStringada)
                            arquivo2.close()
                    arquivo1.close()
    arquivo.close()
                    

def mostrarFaltas(estudanteUsuarioLogar):  ######### TESTAR ESSA FUNCAO, APOS A DE ADICIONAR FALTAS ESTIVER FUNCIONANDO 100%
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding="utf-8")
    for linha in arquivo:
        dados = linha.strip().split()
        if not dados:
            continue
        if dados[3] == estudanteUsuarioLogar:
            arquivo1 = open("DadosDoAluno.txt", "r", encoding="utf-8")
            for linha1 in arquivo1:
                dados1 = linha1.strip().split()
                if not dados1:
                    continue
                if dados1[3] == dados[6]:
                    return print(f"quantidade de faltas{dados1[7]}")
                else:
                    return print("não existe faltas cadastradas")
            arquivo1.close()
    arquivo.close()
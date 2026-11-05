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
                    arquivo.write("tentativa login estudante nome digitado: " + estudanteUsuarioLogar + " " + "senha digitada: " + estudanteSenhaLogar)
                    arquivo.close()
                    return "Login de estudante permitido"
            elif usuario == 2 and dados[9] == "professor":
                if professorUsuarioLogar == dados[3] and professorSenhaLogar == dados[12]:
                    arquivo = open("BancoDeDados.txt", "a", encoding="utf8")
                    arquivo.write("tentativa login professor nome digitado: " + professorUsuarioLogar + " " + "senha digitada: " + professorSenhaLogar)
                    arquivo.close()
                    return "Login de professor permitido"
    arquivo.close()
    return "Login não autorizado"
    


def numero_maquina (numeracao_maquina =""):
    maquinas = []
    maquinas.append(numeracao_maquina)

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
def carregarUsuario(nomes, matriculas, perfis):
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if not linha:
                    continue

                dados = linha.split(SEPARADOR)

                if len(dados) != 3:
                    continue

                nome, matricula, perfil = dados

                nomes.append(nome)
                matriculas.append(matricula)
                perfis.append(perfil)

    except FileNotFoundError:
        pass

#RODOLFO: Função para adicionar novos usuários (lembrar de chamar no código principaç).
def adicionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas):
    senhas123 = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
    import random
    nome = input("Digite o nome do novo usuário: ").strip()
    matricula = random.randint(1000000000, 9999999999)
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

    perfisValidos = ("estudante", "professor")

    if perfil not in perfisValidos:
        print("Perfil inválido!")
        return False

    nomes.append(nome)
    matriculas.append(matricula)
    perfis.append(perfil)
    senhas.append(senhaAleatoria)

    salvarUsuario(nomes, matriculas, perfis)
    senhas123.write(f"\nNome do usuário: {nome} - matrícula: {matricula} - Perfil: {perfil} - Senha: {senhaAleatoria}")
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

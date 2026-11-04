# Função para limpar o terminal. Gustavo:Corrigi, agr ta certo.

def clear_terminal():
    import os, platform
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Função que confirma se a entidade é adm
def confirmacao_adm():
    confirmacao = open("ApenasADM's.txt", "r", encoding="utf-8")
    arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
    hora = datetime.now()
    HorarioAjeitado = hora.strftime("%d/%m/%Y %H:%M")
    tentativas = 5
    erros = 0


    while tentativas > 0:
        usuarioADM = input("Informe o usuario do administrador: ").strip()
        senhaADM = input("Informe a senha do administrador: ").strip()
        osdoisjuntos = usuarioADM+senhaADM

        if osdoisjuntos == confirmacao.readline():
            print("Senha correta, login concluido.")
            return True
        
        tentativas-=1
        erros+=1
        print(f"Senha incorreta {tentativas} tentativas restantes!")

        if erros == 3:
            arquivo.write(f"\nTentativa de login suspeita as {HorarioAjeitado}")
        if erros == 5:
            arquivo.write(f"\nTentativa de invasão as {HorarioAjeitado}")
    print("Acesso negado!")
    return False
    confirmacao.close()
    arquivo.close()    

#LUCAS: TA PRONTO
def logarNormal(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
    estudantesUsuario = []
    estudantesSenha = []
    professorUsuario = []
    professorSenha = []
    arquivo = open("BancoDeContasExistentes.txt", "r", encoding='utf8')
    if usuario == 1:
        estudantesUsuario.append(estudanteUsuarioLogar)
        estudantesSenha.append(estudanteSenhaLogar)
        if estudanteUsuarioLogar in "BancoDeContasExistentes.txt" and estudanteSenhaLogar in "BancoDeContasExistentes.txt"
    elif usuario == 2:
        professorUsuario.append(professorUsuarioLogar)
        professorSenha.append(professorSenhaLogar)

    arquivo.close()    
#def logarNormal(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
#    estudantesUsuario = []
#    estudantesSenha = []
#    professorUsuario = []
#    professorSenha = []
#    arquivo = open("BancoDeDados.txt", "a", encoding='utf8')
#    if usuario == 1:
#        estudantesUsuario.append(estudanteUsuarioLogar)
#        estudantesSenha.append(estudanteSenhaLogar)
#        print("Fazer algo aqui. EX:Ver boletim, ver faltas, etc")
#        arquivo.write("login estudante: " + estudantesUsuario[0] + " " + " senha estudante: " + estudantesSenha[0] + "\n")
#    elif usuario == 2:
#        professorUsuario.append(professorUsuarioLogar)
#        professorSenha.append(professorSenhaLogar)
#        print("pedir senha e fazer algo daqui. EX: publicar notas, adicionar falta, etc")
#        arquivo.write("login professor: " + professorUsuario[0] + " " + " senha professor: " + professorSenha[0] + "\n")
#    arquivo.close()    





#LUCAS:
#ESSA FUNCAO É SO PRA CRIAR O LOGIN, COM NOME E SENHA, SENDO TIPO 1 ESTUDANTE, TIPO 2 PROFESSOR, TIPO 3 ADM

#FALTA ADICIONAR AS VARIARIES PORQUE A PERGUNTA PARA ADICIONAR DENTRO DAS LISTAS NO APPEND() AINDA NAO FORAM-
#-CRIADAS NO INICIO.PY E OBVIAMENTE FALTA ADICIONAR OS PARAMETROS, MAS A FUNCAO EM SI PARA CRIAR O LOGIN É ESSA
def criarNormal(tipo, ):
    estudanteUsuarioADM = []
    estudanteSenhaADM = []
    professorUsuarioADM = []
    professorSenhaADM = []
    admUsuarioADM = []
    admSenhaADM  = []
    arquivo = open("ApenasADM's.txt", "a", encoding='utf8')
    if tipo == 1:
        estudanteUsuarioADM.append()
        estudanteSenhaADM.append()
        arquivo.write("login estudante: " + estudanteUsuarioADM[0] + " " + " senha estudante: " + estudanteSenhaADM[0] + "\n")
    elif tipo == 2:
        professorUsuarioADM.append()
        professorSenhaADM.append()
        arquivo.write("login professor: " + professorUsuarioADM[0] + " " + " senha professor: " + professorSenhaADM[0] + "\n")
    elif tipo == 3:
        admUsuarioADM.append()
        admSenhaADM.append()
        arquivo.write("login adm: " + admUsuarioADM[0] + " " + " senha adm: " + admSenhaADM[0] + "\n")
    arquivo.close()



#LUCAS: ISSO TAVA NUM OUTRO ARQUIVO MAS JA QUE É UMA FUNCAO COPIEI PRA CA
#OBS de Omar: criei aqui so pra explicar mais separado do código principal
from datetime import datetime

print("Estrutura geral do sistema de hórario: ")
hora = datetime.now()
HorarioDeAcesso = hora.strftime("%H")

def timer(HorarioDeAcesso):
    if HorarioDeAcesso >= 7 and HorarioDeAcesso <= 22:
        #(OMAR): isso vai dizer que pelo menos o horário de acesso não é suspeito
        return
    else:
        return "Tente logar em outro horario"
        #nessa parte a gente vai ter que classificar já que a tentativa é suspeita

ARQUIVO_USUARIOS = "BancoDeContasExistentes.txt"
SEPARADOR = ";"

#RODOLFO: Registrar Horário de entrada
def registrarAuditoria(operacao, usuarioAfetado):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("BancoDeContasExistentes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_hora};{operacao};{usuarioAfetado}\n")

#RODOLFO: Isso daqui é pra conferir se o usuário de fato existe, usei ela nas funções de adcionar e excluir usuário.
def salvarUsuario(nomes, matriculas, perfis):
    if not (len(nomes) == len(matriculas) == len(perfis)):
        raise ValueError("Usuário não encontrado ou incoerente com o que foi listado.")

    #with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:
        #for nome, matricula, perfil in zip(nomes, matriculas, perfis):
            #arquivo.write(
                #f"{nome}{SEPARADOR}"
                #f"{matricula}{SEPARADOR}"
                #f"{perfil}\n")

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

#RODOLFO: Função para adcionar novos usuários (lembrar de chamar no código principaç).
def adcionarUsuario(nomes, matriculas, perfis, nome, perfil, senhas):
    import random
    nome = input("Digite o nome do novo usuário: ").strip()
    matricula = random.randint(1000000000, 9999999999)
    perfil = input("Digite o perfil (estudante/professor/administrador): ").strip().lower()
    senhaAleatoria = random.randint(100000000000, 999999999999)
    print(f"Sua senha é: {senhaAleatoria}")

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
    registrarAuditoria("\nNome do usuário"f" {nome} - matrícula: {matricula} - Perfil: {perfil} - Senha: {senhaAleatoria}")
    print("Usuário adicionado com sucesso: ")
    return True


#RODOLFO: Função para excluir o usuário (só chamar lá no código principal agr).
def excluirUsuario(nomes, matriculas, perfis):
    matricula = input("Digite a matrícula do usuário que será exluído: ").strip()

    if matricula not in matriculas:
        print("usuário não encontrado.")
        return False

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

#função ocultar a matricula
"""def matricula_ocultada (matricula_string, letras_visiveis = 2):
    matricula_string = str(matricula)
    matricula = 0
    estrelas = "*" * (len(matricula_string) - letras_visiveis)

    return f"A sua matrícula é a: {matricula_string[:2]}{estrelas}"""""

#revelar = matricula_ocultada()

#print(matricula_ocultada(matricula, 2))
"""def processo_revelar():
    revelar = matricula_ocultada(matricula, 2)
    return revelar"""
#def matricula_revelar():
    
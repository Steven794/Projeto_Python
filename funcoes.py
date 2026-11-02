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
    agora = datetime.now()
    agoraajeitado = agora.strftime("%d/%m/%Y %H:%M")
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

        if erros == 2 :
            arquivo.write(f"\nTentativa de login suspeita as {agoraajeitado} horas")
        if erros == 5:
            arquivo.write(f"\nTentativa de invasão as {agoraajeitado} horas")
        
    return False
    confirmacao.close()
    arquivo.close()    

#LUCAS: TA PRONTO
def logarNormal(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
    estudantesUsuario = []
    estudantesSenha = []
    professorUsuario = []
    professorSenha = []
    arquivo = open("tentativaLogin_tempo.txt", "a", encoding='utf8')
    if usuario == 1:
        estudantesUsuario.append(estudanteUsuarioLogar)
        estudantesSenha.append(estudanteSenhaLogar)
        print("Fazer algo aqui. EX:Ver boletim, ver faltas, etc")
        arquivo.write("login estudante: " + estudantesUsuario[0] + " " + " senha estudante: " + estudantesSenha[0] + "\n")
    elif usuario == 2:
        professorUsuario.append(professorUsuarioLogar)
        professorSenha.append(professorSenhaLogar)
        print("pedir senha e fazer algo daqui. EX: publicar notas, adicionar falta, etc")
        arquivo.write("login professor: " + professorUsuario[0] + " " + " senha professor: " + professorSenha[0] + "\n")
    arquivo.close()





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
        arquivo.writearquivo.write("login estudante: " + estudanteUsuarioADM[0] + " " + " senha estudante: " + estudanteSenhaADM[0] + "\n")
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
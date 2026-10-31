def logar(usuario, estudanteUsuarioLogar="", estudanteSenhaLogar="", professorUsuarioLogar="", professorSenhaLogar=""):
    estudantesUsuario = []
    estudantesSenha = []
    professorUsuario = []
    professorSenha = []
    arquivo = open("texto.txt", "a", encoding='utf8')

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
usuario = int(input("usuario: "))
if usuario == 1:
    estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip().lower()
    estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
    logar(usuario, estudanteUsuarioLogar, estudanteSenhaLogar)
else:
    professorUsuarioLogar = input("Digite o nome do professor: ").strip().lower()
    professorSenhaLogar = input("Digite a senha do professor: ").strip()
    logar(usuario, professorUsuarioLogar=professorUsuarioLogar, professorSenhaLogar=professorSenhaLogar)
def confirmacao_adm():
    while True:
        print("Antes de criar uma conta, diga seu usuário e senha de administrador: ")
        usuarioADM = input("Usuário: ")
        senhaADM = input("Senha: ")
        osdoisjuntos = usuarioADM+senhaADM
        with open("ApenasADM's.txt", "r", encoding="utf-8") as confirmacao:
                    
            if confirmacao.readline() == osdoisjuntos:
    
                print("Certo você acertou a senha.")
    
                usuario = input("Digite o nome do úsuario a ser criado: ")
                senha = input("Digite sua senha, ela tem que ter 8 caractéres: ")
                niveldepermissao = input("O usuário é um Estudante ou um Professor: ")
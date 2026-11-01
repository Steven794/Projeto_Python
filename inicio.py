from datetime import datetime
from funcoes import *
import time # Obs: Perguntar a Carol se pode usar!!!!!!

clear_terminal()

arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhas = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
administradores = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza
tentativadelogin = 0

nomes = []
matriculas1 = []


# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
# OBS omar: to tentando da uma entendida melhor no projeto no que passaram no slide, e acho que a gente é livre pra escolher algumas coisas, além do nome, matricula... a gente podia adicionar pro professor colocar uma nota para tal aluno

while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input(" Se você é um Estudante digite [1]\n Professor digite [2]\n Administrador digite [3] "))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
        logarNormal(usuario, estudanteUsuarioLogar, estudanteSenhaLogar)

    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip()
        professorSenhaLogar = input("Digite a senha do professor: ").strip()
        logarNormal(usuario, professorUsuarioLogar=professorUsuarioLogar, professorSenhaLogar=professorSenhaLogar)
    elif usuario == 3:
        admUsuarioLogar = input("Digite o nome do administrador: ").strip()
        print("Digite [1] caso deseje adicionar.\nDigite [2] para ver os dados informados.\nDigite [3] caso deseje editar um dado.\nDigite [4] para deletar algum dado.\nDigite [5] para encerrar o programa. ")
        opcao = int(input("Digite a opção que você deseja acessar: "))

        if opcao == 1:
            nome = input("Digite o nome: ").strip()
            nomes.append(nome)
            matricula = input("Digite a matrícula: ").strip()
            matriculas1.append(matricula)

        elif opcao == 2:
            print(f"Nome: {nome}")
            print(f"Matricula:{matricula}")

            if usuario == 1:
                print("Perfil: estudante")

            elif usuario == 2:
                print("Perfil: professor")
                
            elif usuario == 3:
                print("Perfil: Administrador")
                
                print("hora: xx horas até yy horas")

        elif opcao == 3:
            indice = int(input("Digite o índice do nome que deseja atualizar: "))
            if 0 <= indice < len(nomes):
                novo_nome = input("Digite o novo nome: ")
                nomes[indice] = novo_nome

            else:
                print("Índice Inválidos! ")

        elif opcao == 4:
            indice = int(input("Digite o índice do nome que deseja deletar: "))
            if 0 <= indice < len(nomes):
                nomes.pop(indice)

            else:
                print("Índice Inválidos! ")

        elif opcao == 5:
            print("Encerrando...")
            break

        else:
            print("Valor invalido!")
            continue

    else:
        print("Valor Invalido!")
        continue

"""    elif OpcaoConta == "1":
        print()
        print("Caso tenha selecionado a opção errada: Escreva 0 para voltar ao ínicio. \nSe não, Digite 1 para continuar")
        opcaocertaouerrada2 = int(input("Resposta: "))
        if opcaocertaouerrada2 == 0:
            break
        elif opcaocertaouerrada2 == 1:
            print("Digite seu usuário e senha. ")
            Usuario = input("Digite seu usuário: ")
            Senha = input("Digite sua senha: ")"""


# OBS Omar:pessoal tudo que ta aqui membaixo deve ficar dentro desses if's de usuarios, cada usuario vai ter uma interação diferente de acordo com seu nivel de Aura
# OBS Omar: IMPORTANTE quando a gente for criar o sistema de segurança a gente NÃO pode colocar a senha no código (tenho 99% de certeza)


arquivo.close()
senhas.close()
administradores.close()

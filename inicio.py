from datetime import datetime
import os
import funcoes
os.system('cls')


arquivo = open("BancoDeDados.txt", "a", encoding="utf-8")
senhas = open("BancoDeContasExistentes.txt", "a", encoding="utf-8")
administradores = open("ApenasADM's.txt", "r", encoding="utf-8")
# OBS  Omar: pessoal a base desse código é um que a gente fez um tempo atras na aula que to modificando com as demandar do projeto, como a parte de adicionar a um arquivo e tals, entao vai ter coisas que a gente vai apagar e outras que utiliza

nomes = []
matriculas = []


# OBS omar: pode ser bom criar uma pasta so de registro de acesso com o nome da pessoa e a classificação
# OBS omar: to tentando da uma entendida melhor no projeto no que passaram no slide, e acho que a gente é livre pra escolher algumas coisas, além do nome, matricula... a gente podia adicionar pro professor colocar uma nota para tal aluno

while True:
    print(" Digite '0' caso deseje criar uma conta (Apenas Administradores podem criar contas). \nDigite '1' caso deseje logar com sua conta")
    OpcaoConta = input("Resposta: ").strip()
    #obs steven: adicionei um strip para nao ter o perigo de deixar o espaço para que a condicional não ignore a comparação 
    if OpcaoConta == "0":
        print(" Caso tenha selecionado a opção errada: Escreva 0 para voltar ao ínicio. \nSe não, Digite 1 para continuar")
        opcaocertaouerrada = int(input("Resposta: "))
        if opcaocertaouerrada == 0:
            break
        elif opcaocertaouerrada == 1:
            while True:
                print("Antes de criar uma conta, diga seu usuário e senha de administrador: ")
                usuarioADM = input("Usuário: ")
                senhaADM = input("Senha: ")
                osdoisjuntos = usuarioADM+senhaADM
                
                if administradores.readline() == osdoisjuntos:

                    print("Certo você acertou a senha.")

                    while True:
                        usuario = input("Digite o nome do úsuario a ser criado: ")
                        senha = input("Digite sua senha, ela tem que ter 8 caractéres: ")
                        niveldepermissao = input("O usuário é um Estudante ou um Professor: ")
                    #obs omar: aqui eu cansei um pouco, dps tem que adicionar pra caso o cara digite certo ou nn e os escambal...
                    # OBS de OMAR: arquivo txt não aceita inteiro so string por isso a senha ta string

                    # OBS IMPORTANTE: NO FINAL QUANDO O CARA CRIAR UMA CONTA TEM QUE TER UM BREAK PORQUE TEM 2 WHILE TRUE
                    if len(senha) == 8:
                        pass  # OBS de OMAR: arquivo txt não aceita inteiro so string por isso a senha ta string
                else:
                    print("Você errou o úsuario ou a senha, tente novamente")

            else:
                print("Você digitou uma opção inválida")
        else:
            print("calma que to terminando essa parte")

    elif OpcaoConta == "1":
        while True:
            print(" Caso tenha selecionado a opção errada: Escreva 0 para voltar ao ínicio. \nSe não, Digite 1 para continuar")
            opcao = int(input("Resposta: "))
            if opcao == 0:
                break
            elif opcao == 1:
                while True:
                    print("Antes de criar uma conta, diga seu usuário e senha de administrador: ")
                    LogarusuarioADM = input("Digite o usuario de ADM para logar: ")
                    LogarsenhaADM = input("Digite a senha de ADM para logar: ")
                    osdoisjuntosLogar = LogarusuarioADM + LogarsenhaADM

                    if administradores.readline() == osdoisjuntosLogar:

            else:
                print("Valor Invalido! Digite um valor válido.")
                continue

    else:
        print("Valor Invalido! Digite um valor válido.")
        continue



while True:
    """OBS Steven: aqui eu atualizei o tipo de entrada, porque vini havia dito que quando nós testar daria muito trabalho digitar a 
    string 'estudante' inteira e facilitaria apenas digitar um numero."""
    usuario = int(input(" Se você é um Estudante digite [1]\n Professor digite [2]\n Administrador [3] "))
    if usuario == 1:
        estudanteUsuarioLogar = input("Digite o nome do estudante: ").strip().lower()
        estudanteSenhaLogar = input("Digite a senha do estudante: ").strip()
        print("Fazer algo aqui")
    elif usuario == 2:
        professorUsuarioLogar = input("Digite o nome do professor: ").strip().lower()
        professorSenhaLogar = input("Digite a senha de profesor: ").strip()
        
        print("pedir senha e fazer algo daqui")
    elif usuario == 3:
        print("pedir senha e mudar tudo que ta embaixa para dentro daqui")
    else:
        print("Valor invalido!")
        continue

# OBS Omar:pessoal tudo que ta aqui membaixo deve ficar dentro desses if's de usuarios, cada usuario vai ter uma interação diferente de acordo com seu nivel de Aura
# OBS Omar: IMPORTANTE quando a gente for criar o sistema de segurança a gente NÃO pode colocar a senha no código (tenho 99% de certeza)

    print("Digite [1] caso deseje adicionar.\nDigite [2] para ver os dados informados.\nDigite [3] caso deseje editar um dado.\nDigite [4] para deletar algum dado.\nDigite [5] para encerrar o programa. ")
    opcao = int(input("Digite a opção que você deseja acessar: "))
    if opcao == 1:
        nome = input("Digite o nome: ").strip()
        nomes.append(nome)
        matricula = input("Digite a matrícula: ").strip()
        matriculas.append(matricula)
    elif opcao == 2:
        # Nome: Gustavo 
        # matricula: 123456
        # perfil: estudante
        # hora: 7 horas ate 18 horas
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
        print("Índice Inválidos! ")

arquivo.close()
senhas.close()
administradores.close()

arquivo = open("DadosDoAluno.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close

linhas[2] = "ola\n"

arquivo1 = open("DadosDoAluno.txt", "w", encoding="utf-8")
arquivo1.writelines(linhas)
arquivo1.close



"""def matriz_maquinas(usuario, nome_aluno, nome_professor, numeracao_maquina):
    logins = 0
    matriz = [[], [], []] #Mari: c1: maquina; c2 nome; c3 perfil
    for linha in range(30): 
        for coluna in range(3):
            matriz[coluna].append(input(f"valor [{linha}][{coluna}]: "))

    for linha in matriz:
        for elemento in matriz:
            print(elemento, end= " ")
        print()

    matriz = []

    for i in range(1, 31):
        linha = []

        while True:
            valor = int(input(f"Insira o valor da linha {i+1} da coluna {j+1}: "))
            linha.append(valor)

        matriz.append(linha)"""
maquinas_repetidas = []
def acesso_maquina (numeracao_maquina):
    with open ("BancoDeDados.txt", "r", encoding="utf-8") as arquivo:
        for i in range(len(maquinas)):
            if numeracao_maquina == maquinas[i]:
                maquinas_repetidas.append(numeracao_maquina)
            

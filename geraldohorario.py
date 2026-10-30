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
        #nessa parte a gente vai ter que classificar já que a tentativa é suspeita
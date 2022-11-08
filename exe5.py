import math

def calcula_porcentagem_sorteio(assinante,minutos_assistidos):

    horas = []
    total_horas = 0
    porcentagem = []

    for minutos in minutos_assistidos:
        horas.append(math.ceil(minutos / 60)) 

    for i in range(0, len(assinante)):
        if assinante[i]:
            horas[i] *= 2
        total_horas += horas[i]

    for hora in horas:
        porcentagem.append(round(hora * 100 / total_horas))
        

    return porcentagem

print(calcula_porcentagem_sorteio([True,False],[60,120]))
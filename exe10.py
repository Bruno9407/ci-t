def shuffle_musicas(musicas_tocadas):
    shuffle = []
    maior = -1
    menor = 999

    if len(musicas_tocadas) % 2 == 0:
        for c in range(0, int(len(musicas_tocadas) / 2)):
            for i, musica in enumerate(musicas_tocadas):
                if i == 0:
                    maior = musica
                    menor = musica
                else:
                    if musica > maior:
                        maior = musica
                    elif musica < menor:
                        menor = musica
            shuffle.append(maior)
            shuffle.append(menor)
            musicas_tocadas.remove(maior)
            musicas_tocadas.remove(menor)
            maior = 0
            menor = 999
    else:
        for c in range(0, int(len(musicas_tocadas) / 2)):
            for i, musica in enumerate(musicas_tocadas):
                if i == 0:
                    maior = musica
                    menor = musica
                else:
                    if musica > maior:
                        maior = musica
                    elif musica < menor:
                        menor = musica
            shuffle.append(maior)
            shuffle.append(menor)
            musicas_tocadas.remove(maior)
            musicas_tocadas.remove(menor)
            maior = 0
            menor = 999
        shuffle.append(musicas_tocadas[0])
           
    return shuffle

print(shuffle_musicas([2,10,5,3]))
from itertools import permutations

def menor_string_maior(name):
   
    permutas = sorted(''.join(chars) for chars in permutations(name))
    permutas.sort(reverse=True)

    for i,permut in enumerate(permutas):
        if i == 0:
            menor = permut
        else:
            if permut > name:
                if permut < menor:
                    menor = permut

    if menor <= name:
        return "sem resposta"
    else:
        return menor

print(menor_string_maior('nextgen'))
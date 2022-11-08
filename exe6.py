def checa_numero_escondido(numero,numero_oculto):

    num = str(numero)
    num_oculto = str(numero_oculto)
    res = ""

    for number in num_oculto:
        if number in num:
            res += number  
    
    if res == num_oculto:
        return True
    else: 
        return False

print(checa_numero_escondido(12345,235))
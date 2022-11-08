def calcula_numero_da_senha(senha):
    valor = ""
    zero = 0
    um = 0
    
    for c in range (0, len(senha)):
        for codigo in senha:
            
            if codigo[c] == "0":
                zero += 1
            elif codigo[c] == "1":
                um += 1
        if um >= zero:
                valor += "1"
        else:
            valor += "0"
        
        zero = 0
        um = 0
    
    decimal = 0
    c = 0
    n = len(valor)
    binario = int(valor)
    while n >= 0:
        resto = binario % 10
        decimal += resto * (2**c)
        n -= 1
        c += 1
        binario = binario // 10

    return decimal

print(calcula_numero_da_senha(["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]))
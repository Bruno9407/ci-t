def calcula_total_leds(altura,largura):
    if largura > 0:   
        largura += 1
    if altura > 0:
        altura += 1

    return largura * altura

print(calcula_total_leds(1,1))
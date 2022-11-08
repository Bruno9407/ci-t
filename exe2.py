def retorna_menor_e_maior_valor_de_vendas(tickets):
    valores = []
    menor = 999999
    maior = 0
    
    for ticket in tickets:
        for i in range (0, len(ticket)):
            if ticket[i] >= 20 and ticket[i] <= 500 and ticket[i] < menor:
                menor = ticket[i]
            elif ticket[i] >= 20 and ticket[i] <= 500 and ticket[i] > maior:
                maior = ticket[i]                   
    valores.append(menor)
    valores.append(maior)
    return valores

print(retorna_menor_e_maior_valor_de_vendas([[200,100],[300]]))
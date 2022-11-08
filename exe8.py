def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    
    print((tf1,vqr1,tf2,vqr2))
    
    distancia = 0.0
    tf1 = float(tf1)
    vqr1 = float(vqr1)
    tf2 = float(tf2)
    vqr2 = float(vqr2)

    if tf1 == tf2 and vqr1 == vqr2:
        return "Tanto faz"
        
    distancia = round((tf2 - tf1) / (vqr1 - vqr2), 2)

   
    if distancia <= 10.0 and distancia > 0.0:
        resposta = f"Empresa 1 quando a distância < {distancia}, Tanto faz quando a distância = {distancia}, Empresa 2 quando a distância > {distancia}"
    elif vqr1 + tf1 < vqr2 + tf2:
        resposta = "Empresa 1"
    elif vqr2 + tf2 < vqr1 + tf1:
        resposta = "Empresa 2"      
       
    return resposta

print(escolhe_taxi("2.5","1.0","5.0","0.75"))
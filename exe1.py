def ultima_parada(combustivel,consumo,postos_de_gasolina):
    distanciaMaxima = combustivel * consumo
    maisDistante = -1
    
    for posto in postos_de_gasolina:
      
      if posto > maisDistante and posto < distanciaMaxima:
        maisDistante = posto
        
    return maisDistante

print(ultima_parada(2,8,[2,15,22,11]))
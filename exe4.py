def calcula_top_ocorrencias_de_queries(texto,queries,k):

    quantidades = {}
    maiores = []
    palavras = texto.split()

    for querry in queries:
        quantidades[querry] = 0         
        for palavra in palavras:
            if querry in palavra:
                quantidades[querry] += 1
  

    for i in sorted(quantidades, key = quantidades.get, reverse=True):
        maiores.append(i)
    maiores = maiores[:k]

    return maiores

print(calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",["a","em","i","el"],2))
    
    
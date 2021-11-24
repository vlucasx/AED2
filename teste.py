
"""""
Implementar um programa (aplicação) para realizar
a distribuição e localização de pedaços de arquivos multimídia de
músicas localizados remotamente em distintos nós de uma rede
de comunicação (e.g., Internet) considerando o paradigma BitTorrent.
Esta aplicação considera a utilização do modelo DHT (Distributed Hash Tables)
e deve ser comparada com o modelo empregado no BitTorrent original.
"""""

import json

def criarHashTable():

    frases = []
    hashFrases = []

    for i in range(91): # aceita: (múltiplos de 3 e de 2 ao mesmo tempo) + 1
        frases.append("essa é a frase"+str(i+1))


    for frase in frases:
        hashFrases.append(hash(frase))

    print("frases:")
    print(frases)
    print(" ")
    print("Hash das frases:")
    print(hashFrases)
    print(" ")

    nos = []

    i=0
    k=1



    distanciaMax = (len(frases)-1)/(2*3)
    print("distmax:",distanciaMax)
    while i < len(frases)-1:

        if k+distanciaMax > (len(frases)-1)/3:
            noDistante = int(abs((len(frases)-1)/3 - (k+distanciaMax)))
        else:
            print("valor de k:", k)
            noDistante = int(k+distanciaMax)

        if i==0:
            anterior = (len(frases)-1)/3

        else:
            anterior = k-1

        if i==len(frases)-4:
            posterior=1
        else:
            posterior=k+1

        no = {
                "nó anterior":anterior, 
                "nóAtual":k,
                "próx nó":posterior,
                "nó distante": noDistante,

                "frase1":frases[i],
                "hashFrase1":hashFrases[i],

                "frase2":frases[i+1],
                "hashFrase2":hashFrases[i+1],

                "frase3":frases[i+2],
                "hashFrase3":hashFrases[i+2],
                }       
        i=i+3        
        k=k+1
        nos.append(no)

    with open('nos.json', 'w', encoding='utf-8') as f:
        json.dump(nos, f, ensure_ascii=False)

    print("Nós:")
    print(nos)

    return nos

def encontrarNoSequencial(nos, numNoInicial, numNoBuscado):
    if numNoInicial == numNoBuscado:
        return nos[numNoInicial-1]

    numNoAtual=numNoInicial
    numBuscas = 0
    while numNoAtual != numNoBuscado:
        numBuscas = numBuscas+1
        print("no atual:",numNoAtual)
        print("no buscado:",numNoBuscado)
        print("prox nó:", nos[numNoAtual-1]["próx nó"])
        print(" ")

        if nos[numNoAtual-1]["nóAtual"] == numNoBuscado:
            print("num de buscas:", numBuscas)
            return nos[numNoAtual-1]

        else:
            numNoAtual=nos[numNoAtual-1]["próx nó"]

            if numNoAtual == numNoBuscado:
                print("num de buscas:", numBuscas)
                return nos[numNoAtual-1]


def encontrarNoPulando(nos, numNoInicial, numNoBuscado):
    if numNoInicial == numNoBuscado:
        return nos[numNoInicial-1]

    numNoAtual=numNoInicial
    numBuscas = 0
    while numNoAtual != numNoBuscado:
        numBuscas = numBuscas+1

        while numNoBuscado >= nos[numNoAtual-1]["nó distante"]:
              
              
              print("nó atual:",numNoAtual)
              print("nó buscado:",numNoBuscado)
              print("nó distante:",nos[numNoAtual-1]["nó distante"])
              print("distancia do nó atual ao nó buscado:",abs(numNoBuscado - numNoAtual))
              print("distancia do nó distante ao nó buscado:", abs(numNoBuscado - nos[numNoAtual-1]["nó distante"]))

              if abs(numNoBuscado - numNoAtual) < abs(numNoBuscado - nos[numNoAtual-1]["nó distante"]):
                  print("distância do nó atual ao nó buscado é menor que a do nó distante ao nó buscado")
                  break
              else:
                    print("pulou para o nó distante")
                    numNoAtual = nos[numNoAtual-1]["nó distante"]
                    numBuscas = numBuscas+1
              print(" ")
            

        print(" ")
        print("no atual:",numNoAtual)
        print("no buscado:",numNoBuscado)
        print("prox nó:", nos[numNoAtual-1]["próx nó"])
        print(" ")

        if nos[numNoAtual-1]["nóAtual"] == numNoBuscado:
            print("num de buscas:", numBuscas)
            return nos[numNoAtual-1]

        else:
            numNoAtual=nos[numNoAtual-1]["próx nó"]

            if numNoAtual == numNoBuscado:
                print("num de buscas:", numBuscas)
                return nos[numNoAtual-1]



if __name__ == "__main__":

    nos=criarHashTable()
    print(" ")
    print("nó encontrado!:", encontrarNoPulando(nos, 1, 20))

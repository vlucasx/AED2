
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

    for i in range(61):
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

    while i <len(frases)-1:
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
                "nó":k,
                "próx nó":posterior,
                
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


def encontrarNo(nos):
    noInicial=2
    noBuscado=4


if __name__ == "__main__":

    criarHashTable()
    
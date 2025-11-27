import random

substantivos = ["casa","pessoa","dia","coisa","vida","mundo","homem","mulher","país","carro","sol"]
verbos = ["ser", "estar", "ter", "fazer","saber","querer","poder","falar", "ver","ouvir","comer", "viver"]
adjetivos = ["bom","mau","grande","pequeno","bonito","feio","feliz","triste","novo","velho","quente"]

def gera_frase():
    frase= random.choice(substantivos) + " " + random.choice(adjetivos) + " " + random.choice(verbos) + " " + random.choice(substantivos) + " " + random.choice(adjetivos)
    return frase

def array_frases(tamanho):
    return [gera_frase() for i in range(tamanho)]

def verifica_termo(array, termo):
    for frase in array:
        if termo in frase:
            print(frase)

def conta_vogais_consoantes(frase):
    vogais_lista= "aeiouAEIOU"
    consoantes_lista= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    qtd_vogais= 0
    qtd_consoantes= 0
    for letra in frase:
        for v in vogais_lista:
            if letra == v:
                qtd_vogais += 1
        for c in consoantes_lista:
            if letra == c:
                qtd_consoantes += 1
    return qtd_vogais, qtd_consoantes

def gera_array(tamanho, inicio, fim):
    return [random.randint(inicio, fim) for i in range(tamanho)]

def gera_matrix(linhas, colunas, inicio, fim):
    matriz = []
    for i in range(linhas):
        matriz.append(gera_array(colunas, inicio, fim))
    return matriz

def imprime_matrix(matriz):
    for linha in matriz:
        print(linha)

def soma_media_matriz(matriz):
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return 0, 0
    total = 0
    for linha in matriz:
        for elemento in linha:
            total += elemento
    num_elementos = len(matriz) * len(matriz[0])
    media = total / num_elementos
    return total, media

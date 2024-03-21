def reverter(i, j):
    if int(i) > len(genoma):
        return genoma
    elif int(j) > len(genoma):
        j = int(len(genoma))
    parte = genoma[slice(int(i), int(j)+1)]
    parte = parte[::-1]
    return genoma[:int(i)] + parte + genoma[int(j)+1:]
 
def transpor(i, j, k):
    if int(i) > len(genoma):
        return genoma
    elif int(j) > len(genoma):
        j = len(genoma)
    return genoma[:int(i)] + genoma[int(j)+1:int(k)+1] + genoma[int(i):int(j)+1] + genoma[int(k)+1:]
 
def combinar(g, i):
    if int(i) > len(genoma):
        i = len(genoma)
    return genoma[:int(i)] + g + genoma[int(i):]
 
def concatenar(g):
    return genoma + g
 
def remover(i, j):
    if int(i) > len(genoma):
        return genoma
    elif int(j) > len(genoma):
        j = len(genoma)
    return genoma[:int(i)] + genoma[int(j)+1:]
 
def buscar(g):
    print(genoma.count(g))
 
def buscar_bidirecional(g):
    print(genoma.count(g) + genoma[::-1].count(g))
 
def mostrar():
    print(genoma)
 
genoma = str(input())
while True:
    entrada = input().split()
    if entrada[0] == 'reverter':
        genoma = reverter(entrada[1], entrada[2])
    elif entrada[0] == 'transpor':
        genoma = transpor(entrada[1], entrada[2], entrada[3])
    elif entrada[0] == 'combinar':
        genoma = combinar(entrada[1], entrada[2])
    elif entrada[0] == 'concatenar':
        genoma = concatenar(entrada[1])
    elif entrada[0] == 'remover':
        genoma = remover(entrada[1], entrada[2])
    elif entrada[0] == 'transpor_e_reverter':
        genoma = transpor(entrada[1], entrada[2], entrada[3])
        genoma = reverter(entrada[1], entrada[3])
    elif entrada[0] == 'buscar':
        buscar(entrada[1])
    elif entrada[0] == 'buscar_bidirecional':
        buscar_bidirecional(entrada[1])
    elif entrada[0] == 'mostrar':
        mostrar()
    elif entrada == 'sair':
        break
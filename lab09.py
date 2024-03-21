mapa = []
linhas = int(input())
 
 
for _ in range(linhas):
    mapa.append(input().split())
 
 
def anda(robo):
    """
    Faz o robô andar
    :param robo: posição do robô
    :return: None
    """
    i, j = robo
    if (j == len(mapa[0])-1 and i % 2 == 0) or (j == 0 and i % 2 != 0 and i != 0):
        mapa[i][j] = '.'
        mapa[i+1][j] = 'r'
    else:
        if i % 2 == 0:
            mapa[i][j] = '.'
            mapa[i][j+1] = 'r'
        else:
            mapa[i][j] = '.'
            mapa[i][j-1] = 'r'
    imprime()
 
 
def passa_vassoura(robo, sujeira):
    """
    Limpa as sujeiras nas adjacências do robô
    :param robo: posição do robô no mapa
    :param sujeira: posição da sujeira na adjacência do robô
    :return: None
    """
    robo_i, robo_j = robo
    sujeira_i, sujeira_j = sujeira
    if tem_sujeira(robo):
        mapa[robo_i][robo_j] = '.'
        mapa[sujeira_i][sujeira_j] = 'r'
    imprime()
 
 
def tem_sujeira(robo):
    """
    Verifica se há ou não sujeiras nas adjacências do robô
    :param robo: posição do robô no mapa
    :return: retorna a posição da sujeira nas adjacências do robô, se houver
    """
    i, j = robo
    if 1 <= j and mapa[i][j-1] == 'o':
        return i, j-1
    elif 1 <= i and mapa[i-1][j] == 'o':
        return i-1, j
    elif j <= len(mapa[0])-2 and mapa[i][j+1] == 'o':
        return i, j+1
    elif i <= linhas-2 and mapa[i+1][j] == 'o':
        return i+1, j
 
 
def cade_robo():
    """
    Retorna a posição do robô no mapa
    :return: posição do robô no mapa
    """
    for linha in range(len(mapa)):
        for elemento in range(len(mapa[linha])):
            if mapa[linha][elemento] == 'r':
                return linha, elemento
 
 
def volta_pro_lugar(robo_antes, robo_depois):
    """
    Faz com que o robô volte para o lugar em que ele iniciou o modo 'limpando'
    :param robo_antes: posição do robô antes de começar a limpar as sujeiras
    :param robo_depois: posição do robô depois de começar a limpar as sujeiras
    :return: None
    """
    antes_i, antes_j = robo_antes
    depois_i, depois_j = robo_depois
    while depois_j != antes_j:
        if depois_j > antes_j:
            mapa[depois_i][depois_j] = '.'
            depois_j -= 1
            mapa[depois_i][depois_j] = 'r'
        else:
            mapa[depois_i][depois_j] = '.'
            depois_j += 1
            mapa[depois_i][depois_j] = 'r'
        imprime()
    while depois_i != antes_i:
        if depois_i > antes_i:
            mapa[depois_i][depois_j] = '.'
            depois_i -= 1
            mapa[depois_i][depois_j] = 'r'
        else:
            mapa[depois_i][depois_j] = '.'
            depois_i += 1
            mapa[depois_i][depois_j] = 'r'
        imprime()
 
 
def imprime():
    """
    Imprime o mapa do cômodo no formato adequado
    :return: None
    """
    for linha in mapa:
        contador = 0
        for elemento in linha:
            if contador == len(linha)-1:
                print(elemento)
            else:
                print(elemento, end=' ')
            contador += 1
    print()
 
 
def termina(robo):
    i, j = robo
    if linhas % 2 == 0 and i == linhas -1 and j == 0: # caso o número de linhas for par e o robô esteja na primeira coluna da última linha,
        # ele deve voltar para a última coluna da última linha.
        while j != len(mapa[0]) -1:
            robo = cade_robo()
            i, j = robo
            mapa[i][j] = '.'
            mapa[i][j+1] = 'r'
            imprime()
 
 
def main():
    imprime()
    while True:
        robo = cade_robo()
        while True:
            robo_temp = cade_robo()
            if robo[0] == robo_temp[0]: # Se a posição inicial e a temporária estiverem na mesma linha
                robo = robo_temp # a posição inicial se torna a temporária
            elif robo[1] == robo_temp[1]:
                if robo[0] % 2 == 0 and robo[1] == len(mapa[0])-1:
                    robo = robo_temp
                elif robo[0] % 2 != 0 and robo[1] == 0:
                    robo = robo_temp
            if tem_sujeira(robo_temp):
                robo_temp = cade_robo() # Vê a posição temporária do robô após limpar a sujeira
                sujeira = tem_sujeira(robo_temp)
                passa_vassoura(robo_temp, sujeira) # Muda diretamente no mapa a posição do robô e limpa a sujeira
            else:
                break
        if robo[0] == robo_temp[0]:
            robo = robo_temp
            termina(robo_temp) 
            anda(robo_temp) 
        elif robo[1] == robo_temp[1]:
            if robo[0] % 2 == 0 and robo[1] == len(mapa[0])-1:
                robo = robo_temp
                anda(robo_temp)
            elif robo[0] % 2 != 0 and robo[1] == 0:
                robo = robo_temp
                anda(robo_temp)
            else:
                volta_pro_lugar(robo, robo_temp) # caso a posição final do robô após limpar as sujeiras e a 
                # inicial estiverem na mesma coluna, mas essa coluna não for nem a última nem a primeira, o robô deve voltar à posição inicial 
        else:
            volta_pro_lugar(robo, robo_temp)
 
 
if __name__ == '__main__':
    main()
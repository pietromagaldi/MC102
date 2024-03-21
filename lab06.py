def soma_vetores(v1: list[int], v2: list[int]) -> list[int]:
    """
    Soma elemento a elemento de dois vetores
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor resultante
    """
    v3 = []
    for i in range(max(len(v1), len(v2))):
        try: 
            v3.append(v1[i] + v2[i]) 
        except IndexError: 
            try: 
                v3.append(v1[i]) 
            except IndexError: 
                v3.append(v2[i]) 
    return v3
 
 
def subtrai_vetores(v1: list[int], v2: list[int]) -> list[int]:
    """
    Subtrai elemento a elemento de dois vetores
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor resultante
    """
    v3 = []
    for i in range(max(len(v1), len(v2))):
        try:
            v3.append(v1[i] - v2[i])
        except IndexError:
            try:
                v3.append(v1[i])
            except IndexError:
                v3.append(v2[i] * -1)
    return v3
 
 
def multiplica_vetores(v1: list[int], v2: list[int]) -> list[int]:
    """
    Multiplica elemento a elemento de dois vetores
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor resultante
    """
    v3 = []
    for i in range(max(len(v1), len(v2))):
        try:
            v3.append(v1[i] * v2[i])
        except IndexError:
            try:
                v3.append(v1[i])
            except IndexError:
                v3.append(v2[i])
    return v3
 
 
def divide_vetores(v1: list[int], v2: list[int]) -> list[int]:
    """
    Realiza a divisão inteira elemento a elemento de dois vetores
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor resultante
    """
    v3 = []
    for i in range(max(len(v1), len(v2))):
        try:
            v3.append(v1[i] // v2[i])
        except IndexError:
            try:
                v3.append(v1[i])
            except IndexError:
                v3.append(0)
    return v3
 
 
def multiplicacao_escalar(v1: list[int], n: int) -> list[int]:
    """
    Multiplica todos os elementos de um vetor por um escalar
    :param v1: vetor
    :param n: escalar
    :return: vetor resultante
    """
    v3 = []
    for i in v1:
        v3.append(i * n)
    return v3
 
 
def n_duplicacao(v1: list[int], n: int) -> list[int]:
    """
    Duplica o tamanho de um vetor n vezes
    :param v1: vetor
    :param n: escalar
    :return: vetor resultante
    """
    v3 = []
    for i in range(n):
        v3.extend(v1)
    return v3
 
 
def soma_elementos(v1: list[int]) -> int:
    """
    Soma todos os elementos de um vetor
    :param v1: vetor
    :return: vetor cujo único elemento é o resultado da operação
    """
    # OBS: RETORNAR UM VETOR DE ELEMENTO ÚNICO, E NÃO APENAS UM INTEIRO 
    soma = 0
    for i in v1:
        soma += i
    return soma
 
 
def produto_interno(v1: list[int], v2: list[int]) -> int:
    """
    Multiplica elemento a elemento e depois soma os resultados dos produtos
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor cujo único elemento é o resultado da operação
    """
    # OBS: RETORNAR UM VETOR DE ELEMENTO ÚNICO, E NÃO APENAS UM INTEIRO
    v3 = []
    soma = 0
    for i in range(max(len(v1), len(v2))):
        try:
            v3.append(v1[i] * v2[i]) 
        except IndexError: 
            try: 
                v3.append(v1[i]) 
            except IndexError: 
                v3.append(v2[i]) 
    for j in v3: 
        soma += j 
    return soma
 
 
def multiplica_todos(v1: list[int], v2: list[int]) -> list[int]:
    """
    Multiplica cada elemento do primeiro vetor a todos do
    segundo e soma os resultados
    :param v1: vetor 1
    :param v2: vetor 2
    :return: vetor resultante
    """
    v3 = []
    soma = 0
    for i in range(len(v1)):
        for j in range(len(v2)):
            soma += v1[i] * v2[j]
        v3.append(soma)
        soma = 0
    return v3
 
 
def correlacao_cruzada(v1: list[int], v2: list[int]) -> list[int]:
    """
    Utiliza uma máscara para calcular o produto interno entre ela e o vetor
    :param v1: vetor 1
    :param v2: máscara
    :return: vetor resultante
    """
    v3 = []
    f = 0
    for i in range(len(v1)+1):
        if i >= len(v2):
            v3.append(produto_interno(v1[f:i], v2))
            f += 1
    return v3
 
 
def main() -> None:
    """
    Função principal
    :return: Nenhum
    """
    voriginal = list(map(int, input().split(',')))
    while True:
        entrada = str(input()) 
        if entrada == 'soma_vetores':
            vinput = list(map(int, input().split(',')))
            voriginal = soma_vetores(voriginal, vinput)
            print(voriginal)
        elif entrada == 'subtrai_vetores':
            vinput = list(map(int, input().split(',')))
            voriginal = subtrai_vetores(voriginal, vinput)
            print(voriginal)
        elif entrada == 'multiplica_vetores':
            vinput = list(map(int, input().split(',')))
            voriginal = multiplica_vetores(voriginal, vinput)
            print(voriginal)
        elif entrada == 'divide_vetores':
            vinput = list(map(int, input().split(',')))
            voriginal = divide_vetores(voriginal, vinput)
            print(voriginal)
        elif entrada == 'multiplicacao_escalar':
            ninput = int(input())
            voriginal = multiplicacao_escalar(voriginal, ninput)
            print(voriginal)
        elif entrada == 'n_duplicacao':
            ninput = int(input())
            voriginal = n_duplicacao(voriginal, ninput)
            print(voriginal)
        elif entrada == 'soma_elementos':
            voriginal = [soma_elementos(voriginal)]
            print(voriginal)
        elif entrada == 'produto_interno':
            vinput = list(map(int, input().split(',')))
            voriginal = [produto_interno(voriginal, vinput)]
            print(voriginal)
        elif entrada == 'multiplica_todos':
            vinput = list(map(int, input().split(',')))
            voriginal = multiplica_todos(voriginal, vinput)
            print(voriginal)
        elif entrada == 'correlacao_cruzada':
            vinput = list(map(int, input().split(',')))
            voriginal = correlacao_cruzada(voriginal, vinput)
            print(voriginal)
        elif entrada == 'fim':
            break
 
 
if __name__ == '__main__':
    main()
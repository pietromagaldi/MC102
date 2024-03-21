f = int(input()) 
  
filmes = [] 
linhas = [] 
  
categorias = { 
    'filme que causou mais bocejos': {}, 
    'filme que foi mais pausado': {}, 
    'filme que mais revirou olhos': {}, 
    'filme que não gerou discussão nas redes sociais': {}, 
    'enredo mais sem noção': {} 
} 
  
for _ in range(f): 
    filmes.append(input()) 
for k in categorias: 
    for filme in filmes: 
        categorias[k][filme] = [0, 0]  # Os elementos da lista são, respectivamente, a soma das notas e o número de notas recebidas 
  
# Atribuição dos valores da entrada ao dicionário 'categorias' 
q = int(input()) 
for _ in range(q): 
    leitura = input().split(', ') 
    categorias[leitura[1]][leitura[2]][0] += (int(leitura[3])) 
    categorias[leitura[1]][leitura[2]][1] += 1 
 
vencedores = {
    'filme que causou mais bocejos': '',
    'filme que foi mais pausado': '',
    'filme que mais revirou olhos': '',
    'filme que não gerou discussão nas redes sociais': '',
    'enredo mais sem noção': ''
}
 
# Cálculo das médias gerais dos filmes e do total de votos para cada filme 
medias = [0 for i in range(len(filmes))]  # Aqui, criamos uma lista com vários zeros, que posteriormente serão preenchidos com as médias gerais de cada filme 
votos = [0 for i in range(len(filmes))]  # Mesma coisa, mas para os votos totais 
for filme in filmes: 
    for chave in categorias: 
        contador = 0 
        for valor in categorias[chave].values(): 
            if valor[1] != 0: 
                medias[contador] += valor[0] / valor[1] 
            votos[contador] += valor[1] 
            contador += 1 
  
# Cálculo do vencedor de cada categoria com base nas médias 
filme_vencedor = '' 
for j in vencedores: 
    maximo = [0] 
    for k, h in categorias[j].items(): 
        if h[1] != 0: 
            if h[0] / h[1] > maximo[0]: 
                filme_vencedor = k 
                maximo = [h[0] / h[1], h[1]]  # Aqui, guardamos a média máxima como primeiro elemento e o denominador (número de notas recebidas) como segundo 
            elif h[0] / h[1] == maximo[0]: 
                if h[1] > maximo[1]:  # Se o número de notas recebidas pelo primeiro filme for maior que o do máximo, levando em consideração que suas médias aritméticas são iguais, ele vira o novo máximo 
                    maximo = [h[0] / h[1], h[1]] 
                    filme_vencedor = k 
    vencedores[j] = filme_vencedor 
  
# Verificação do prêmio "pior filme do ano" 
lista_vencedores = [i for i in vencedores.values()] 
pior_filme = '' 
maximo = -5 
for filme in vencedores.values(): 
    if lista_vencedores.count(filme) > maximo:  # Se o número de vezes que algum filme aparecer na lista dos vencedores for maior que o máximo 
        maximo = lista_vencedores.count(filme) 
        pior_filme = filme 
    elif lista_vencedores.count(filme) == maximo: 
        if medias[filmes.index(filme)] > medias[filmes.index(pior_filme)]:  # Se a média do filme analisado for maior que a média do pior filme até o momento, ele se tornará o pior filme 
            pior_filme = filme 
  
# Verificação do prêmio "Não Merecia Estar Aqui" 
nao_merecia_estar_aqui = [] 
for i in range(len(votos)): 
    if votos[i] == 0: 
        nao_merecia_estar_aqui.append(filmes[i]) 
 
# Saída
print('#### abacaxi de ouro ####')
print()
print('categorias simples')
for k, v in vencedores.items():
    print(f'categoria: {k}\n- {v}')
print()
print('categorias especiais')
print(f'prêmio pior filme do ano\n- {pior_filme}')
print(f'prêmio não merecia estar aqui\n- ', end='')
if nao_merecia_estar_aqui == []:
    print('sem ganhadores')
else:
    for perdedor in nao_merecia_estar_aqui:
        if perdedor == nao_merecia_estar_aqui[-1]:
            print(perdedor)
        else:
            print(f'{perdedor}, ', end='')
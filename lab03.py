num_jog = int(input())
num_magico = list(map(int, input().split()))
intervalos1 = list(map(int, input().split()))
resultados = []
intervalos2 = []
for i in range(len(intervalos1)):
    if i % 2 != 0:
        intervalos2.append(intervalos1[i]-intervalos1[i-1])
for c in range(num_jog):
    if c+1 <= int(num_jog/2):
        resultados.append(intervalos2[c]*num_magico[c])
    else:
        resultados.append(intervalos2[c]+num_magico[c])
if resultados.count(max(resultados)) == 1:
    print(f'O jogador número {resultados.index(max(resultados)) + 1} vai receber o melhor', end='')
    print(f' bolo da cidade pois venceu com {max(resultados)} ponto(s)!')
else:
    print('Rodada de cerveja para todos os jogadores!')
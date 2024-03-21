class Maquina:
    def __init__(self, vida, pts_ataque, qtd_partes):
        self._vida = vida
        self._pts_ataque = pts_ataque
        self._qtd_partes = qtd_partes
        self._partes_do_corpo = {}
 
    def __str__(self):
        return (f'Pontos de vida: {self._vida}\n'
                f'Pontos de ataque: {self._pts_ataque}\n'
                f'Quantidade de partes: {self._qtd_partes}\n'
                f'Partes do corpo: {self._partes_do_corpo}')
 
    @property
    def vida(self):
        return self._vida
 
    @property
    def pts_ataque(self):
        return self._pts_ataque
 
    @property
    def qtd_partes(self):
        return self._qtd_partes
    
    @property
    def partes_do_corpo(self):
        return self._partes_do_corpo
 
    @vida.setter
    def vida(self, numero):
        self._vida = numero
 
    @pts_ataque.setter
    def pts_ataque(self, numero):
        self._pts_ataque = numero
 
    @qtd_partes.setter
    def qtd_partes(self, numero):
        self._qtd_partes = numero
 
    @partes_do_corpo.setter
    def partes_do_corpo(self, dicionario):
        self._partes_do_corpo = dicionario
 
 
class Parte_do_corpo:
    def __init__(self, fraqueza, dano_max, x, y):
        self._fraqueza = fraqueza
        self._dano_max = dano_max
        self._x = x
        self._y = y
 
    def __str__(self):
        return (f'Fraqueza: {self._fraqueza}'
                f'Dano máximo: {self._dano_max}'
                f'Ponto crítico: {self._x}, {self._y}')
 
    @property
    def fraqueza(self):
        return self._fraqueza
 
    @property
    def dano_max(self):
        return self._dano_max
 
    @property
    def x(self):
        return self._x
 
    @property
    def y(self):
        return self._y
 
    @fraqueza.setter
    def fraqueza(self, string):
        self._fraqueza = string
 
    @dano_max.setter
    def dano_max(self, numero):
        self._dano_max = numero
 
    @x.setter
    def x(self, numero):
        self._x = numero
 
    @y.setter
    def y(self, numero):
        self._y = numero
 
 
def revive(vida_a, vida_m):
    vida_a += vida_m//2
    if vida_a > vida_m:
        vida_a = vida_m
    return vida_a
 
 
vida_max = vida_atual = int(input())
quant_flechas = {}
flechas = input().split()
quant_monstros = int(input())
lista_monstros = []
n_rodada = 1
monstros_derrotados = 0
flechas_atual = {}
acertos_criticos = {}
lista_derrotados = []
 
for elemento in range(0, len(flechas), 2):
    quant_flechas[flechas[elemento]] = flechas[elemento + 1]
 
n_combate = 0
 
# Combate
 
while monstros_derrotados < quant_monstros: 
 
    flechas_atual = quant_flechas.copy()
    n_rodada = 1
    maqs_por_combate = int(input())
    criticos = 0
    vida_atual1 = vida_atual
    monstros_derrotadost = 0
    lista_derrotados.clear()
    acertos_criticos = {}
    j = 0
 
    for k in range(maqs_por_combate):
        leitura = input().split()
        maquina = Maquina(int(leitura[0]), int(leitura[1]), int(leitura[2]))
        lista_monstros.append(maquina)
        for a in range(maquina.qtd_partes):
            leitura = input().split(', ')
            parte_do_corpo = Parte_do_corpo(leitura[1], int(leitura[2]), int(leitura[3]), int(leitura[4]))
            maquina.partes_do_corpo[leitura[0]] = parte_do_corpo
 
    for maquina in range(maqs_por_combate):
        acertos_criticos[maquina] = {}
        for parte_do_corpo in lista_monstros[maquina].partes_do_corpo.keys():
            acertos_criticos[maquina][parte_do_corpo] = [(lista_monstros[maquina].partes_do_corpo[parte_do_corpo].x,
                                                          lista_monstros[maquina].partes_do_corpo[parte_do_corpo].y), 0]
 
    monstros_temp = lista_monstros.copy()
 
    while True:
 
        leitura = input().split(', ')
        parte_do_corpo = monstros_temp[int(leitura[0])].partes_do_corpo[leitura[1]]
        monstro = monstros_temp[int(leitura[0])]
        dano_feito = parte_do_corpo.dano_max - (abs(int(leitura[3]) - parte_do_corpo.x) + abs(int(leitura[4]) -
                                                                                                parte_do_corpo.y))
        if dano_feito < 0:
            dano_feito = 0
        dano_recebido = 0
 
        if (abs(int(leitura[3]) - parte_do_corpo.x) + abs(int(leitura[4]) - parte_do_corpo.y)) == 0:
            criticos += 1
            acertos_criticos[lista_monstros.index(monstro)][leitura[1]][1] += 1
 
        if leitura[2] == parte_do_corpo.fraqueza or parte_do_corpo.fraqueza == 'todas':
            monstro.vida -= dano_feito
            flechas_atual[leitura[2]] = int(flechas_atual[leitura[2]]) - 1
        else:
            monstro.vida -= (dano_feito // 2)
            flechas_atual[leitura[2]] = int(flechas_atual[leitura[2]]) - 1
        
        if monstro.vida <= 0:
            lista_derrotados.append(monstros_temp.index(monstro))
            monstros_derrotadost += 1
            monstros_derrotados += 1
            lista_monstros.remove(monstro)
 
        for maquina in range(maqs_por_combate - monstros_derrotadost):
            dano_recebido += lista_monstros[maquina].pts_ataque
 
        if n_rodada % 3 == 0 and n_rodada != 0:
            vida_atual -= dano_recebido
        
        for chave, flecha in flechas_atual.items():
            flechas_atual[chave] = int(flecha)
 
        if vida_atual <= 0:
            print(f'Combate {n_combate}, vida = {vida_atual1}')
            if monstros_derrotadost != 0:
                for i in lista_derrotados:
                    print(f'Máquina {i} derrotada')
            print(f'Vida após o combate = 0')
            print('Aloy foi derrotada em combate e não retornará a tribo.')
            break
 
        elif monstros_derrotadost == maqs_por_combate:
            print(f'Combate {n_combate}, vida = {vida_atual1}')
            for i in lista_derrotados:
                print(f'Máquina {i} derrotada')
            print(f'Vida após o combate = {vida_atual}')
            print(f'Flechas utilizadas:')
            for tipo, quant in quant_flechas.items():
                if int(quant) - int(flechas_atual[tipo]) > 0:
                    print(f'- {tipo}: {int(quant)-int(flechas_atual[tipo])}/{quant}')
            if criticos != 0:
                print('Críticos acertados:')
                for chave in acertos_criticos.keys():
                    j = 0
                    for a in acertos_criticos[chave].values():
                        if a[1] > 0 and j == 0:
                            print(f'Máquina {chave}:')
                            print(f'- {a[0]}: {a[1]}x')
                            j += 1
                        elif a[1] > 0:
                            print(f'- {a[0]}: {a[1]}x')
            vida_atual = revive(vida_atual, vida_max)
            break
 
        elif max(flechas_atual.values()) == 0:
            print(f'Combate {n_combate}, vida = {vida_atual1}')
            if monstros_derrotadost != 0:
                for i in lista_derrotados:
                    print(f'Máquina {i} derrotada')
            print(f'Vida após o combate = {vida_atual}')
            print('Aloy ficou sem flechas e recomeçará sua missão mais preparada.')
            break
 
        n_rodada += 1
    n_combate += 1
 
if monstros_derrotados == quant_monstros:
    print('Aloy provou seu valor e voltou para sua tribo.')
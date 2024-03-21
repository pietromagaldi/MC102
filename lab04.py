tudo = []
lista_brigam = []
proceds = []
animais_atend =[]
animais_n_atend =[]
animais_indisp = []
animais = []
c = 0
brigas = 0
dias = int(input())
for k in range(dias):
    quant_pares_brigam = int(input())
    for m in range(quant_pares_brigam):
        lista_brigam.append(input().split())
    proceds_disps = input().split()
    for h in range(1, len(proceds_disps), 2):
        proceds_disps[h] = int(proceds_disps[h])
    quant_animais = int(input())
    for l in range(quant_animais):
        tudo.append(input().split())
    for o in range(len(tudo)):
        animais.append(tudo[o][0])
        proceds.append(tudo[o][1])
    for r in range(len(lista_brigam)):
        if lista_brigam[r][0] in animais and lista_brigam[r][1] in animais:
            brigas += 1
    for procedimento in proceds:
        if procedimento not in proceds_disps:
            animais_indisp.append(animais[c])
        else:
            if proceds_disps[proceds_disps.index(procedimento) + 1] == 0:
                animais_n_atend.append(animais[c])
            else:
                animais_atend.append(animais[c])
                proceds_disps[proceds_disps.index(procedimento) + 1] -= 1
        c += 1
    print(f'Dia: {k+1}')
    print(f'Brigas: {brigas}')
    if len(animais_atend) != 0:
        print('Animais atendidos: ', end='')
        for nome in animais_atend:
            if nome == animais_atend[-1]:
                print(nome)
            else:
                print(f'{nome}, ', end='')
    if len(animais_n_atend) != 0:
        print('Animais não atendidos: ', end='')
        for j in animais_n_atend:
            if j == animais_n_atend[-1]:
                print(j)
            else:
                print(f'{j}, ', end='')
    if len(animais_indisp) != 0:
        for g in animais_indisp:
            print(f'Animal {g} solicitou procedimento não disponível.')
    print()
    lista_brigam.clear()
    proceds.clear()
    animais_atend.clear()
    animais_n_atend.clear()
    animais_indisp.clear()
    animais.clear()
    tudo.clear()
    c = 0
    brigas = 0
print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux.', end=' ')
print('Responda a algumas poucas perguntas para ter uma recomendação.')
print('Seu SO anterior era Linux?' )
print('(0) Não')
print('(1) Sim')
resp = int(input())
if resp == 0:
    print('Seu SO anterior era um MacOS?')
    print('(0) Não')
    print('(1) Sim')
    resp = int(input())
    if resp == 0:
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, ', end='')
        print('as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.')
    elif resp == 1:
        print('Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto,', end='')
        print(' as distribuições recomendadas são: ElementaryOS, ApricityOS.')
    else:
        print('Opção inválida, recomece o questionário.')
elif resp == 1:
    print('É programador/ desenvolvedor ou de áreas semelhantes?')
    print('(0) Não')
    print('(1) Sim')
    print('(2) Sim, realizo testes e invasão de sistemas')
    resp = int(input())
    if resp == 0:
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, ', end='')
        print('as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.')
    elif resp == 2:
        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições ', end='')
        print('que servirão de base para seu aprendizado são: Kali Linux, Black Arch.')
    elif resp == 1:
        print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?')
        print('(0) Não')
        print('(1) Sim')
        resp = int(input())
        if resp == 0:
            print('Já utilizou Arch Linux?')
            print('(0) Não')
            print('(1) Sim')
            resp = int(input())
            if resp == 0:
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições ', end='')
                print('que servirão de base para seu aprendizado são: Antergos, Arch Linux.')
            elif resp == 1:
                print('Suas escolhas te levaram a um caminho repleto de desafios, ', end='')
                print('para você recomendamos as distribuições: Gentoo, CentOS, Slackware.')
            else:
                print('Opção inválida, recomece o questionário.')
        elif resp == 1:
            print('Já utilizou Debian ou Ubuntu?')
            print('(0) Não')
            print('(1) Sim')
            resp = int(input(''))
            if resp == 0:
                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que ', end='')
                print('servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.')
            elif resp == 1:
                print('Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos ', end='')
                print('as distribuições: Manjaro, ApricityOS.')
            else:
                print('Opção inválida, recomece o questionário.')
        else:
            print('Opção inválida, recomece o questionário.')
    else:
        print('Opção inválida, recomece o questionário.')
else:
    print('Opção inválida, recomece o questionário.')
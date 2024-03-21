sheila = str(input())
reginaldo = str(input())
 
if sheila == reginaldo:
    print('empate')
elif sheila == 'tesoura' and reginaldo in ['papel', 'lagarto']:
    print('Interestelar')
elif sheila == 'papel' and reginaldo in ['pedra', 'spock']:
    print('Interestelar')
elif sheila == 'pedra' and reginaldo in ['lagarto', 'tesoura']:
    print('Interestelar')
elif sheila == 'lagarto' and reginaldo in ['spock', 'papel']:
    print('Interestelar')
elif sheila == 'spock' and reginaldo in ['tesoura', 'pedra']:
    print('Interestelar')
else:
    print('Jornada nas Estrelas')
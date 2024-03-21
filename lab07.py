operacao = str(input())
busca1 = str(input())
busca2 = str(input())
linhas = int(input())
msg_junta = ''
msg_decod = ''
chave = 0
for i in range(linhas):
    if i+1 != linhas:
        msg_junta += str(input()) + '\n'
    else:
        msg_junta += str(input())
if busca1 == 'vogal':
    for i in msg_junta:
        if i.lower() in 'aeiou':
            busca1 = i
            break
elif busca1 == 'numero':
    for i in msg_junta:
        if i.lower() in '1234567890':
            busca1 = i
            break
elif busca1 == 'consoante':
    for i in msg_junta:
        if i.lower() in 'bcdfghjklmnpqrstvwxyz':
            busca1 = i
            break
if busca2 == 'vogal': 
    for i in msg_junta: 
        if i.lower() in 'aeiou': 
            busca2 = i 
            break 
elif busca2 == 'numero': 
    for i in msg_junta: 
        if i.lower() in '1234567890': 
            busca2 = i 
            break 
elif busca2 == 'consoante': 
    for i in msg_junta: 
        if i.lower() in 'bcdfghjklmnpqrstvwxyz': 
            busca2 = i 
            break 
la = msg_junta[:msg_junta.index(busca1)].count('\n') 
lb = msg_junta[:msg_junta.index(busca2)].count('\n')
if msg_junta.index(busca2) < msg_junta.index(busca1):
    novob = msg_junta[msg_junta.index(busca1):].index(busca2) + msg_junta.index(busca1)
    lb = msg_junta[:novob].count('\n')
    c = novob - lb
else:
    c = msg_junta.index(busca2) - lb
exec(f'a={msg_junta.index(busca1) - la}; b={c}; chave=a{operacao}b')
for k in msg_junta:
    a = (ord(k) + chave) -32
    if k == '\n':
        msg_decod += '\n'
    elif ord(k) + chave > 126:
        msg_decod += chr(32+(a%95))
    elif ord(k) + chave < 32:
        msg_decod += chr(127 - (32 - (ord(k) + chave)))
    else:
        msg_decod += chr(ord(k) + chave)
print(chave)
print(msg_decod)
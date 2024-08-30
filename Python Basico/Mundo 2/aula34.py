from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador sortear algo

print('-=-' * 20)
print('Vou pensar em um numero 0 e 5. Tente adivinhar :D')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) #Jogador tente adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Parabens você conseguiu me vencer')    
else:
    print(f'Ganhei! eu pensei no numero {computador} e não no {jogador}')
    

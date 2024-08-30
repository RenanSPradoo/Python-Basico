from datetime import date

atual = date.today().year
totalMaior = 0
totalMenor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}° pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.')
print(f'E também tivemos {totalMenor} pessoas menores de idade.')
print('=' * 20)
print('10 TEMOS DE UMA PA')
print('=' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo + razao, razao):
    print(f'{i}', end='→ ')
print('ACABOU')

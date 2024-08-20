print('=' * 20)
print('10 TEMOS DE UMA PA')
print('=' * 20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo + razao, razao):
    print(f'{i}', end='→ ')
print('ACABOU')
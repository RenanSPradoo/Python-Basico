print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f' {termo} ', end=' ➜ ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'\nPrograssão finalizada com {total} termos mostrados.')
print()

num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}.')

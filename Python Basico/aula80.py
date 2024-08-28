numeros = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite mais um numero: ')),
        int(input('Digite o ultimo numero: '))
)
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu: {numeros.count(9)} vezes') #count quantoss 9 apareceu na tupla

if 3 in numeros:
    print(f'O valor 3 apareceu na tal: {numeros.index(3)+1}ª posição') #index seria em que lugar o valor 3 apareceu primeiro
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
listaNum = []
maior = 0
menor = 0

for i in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para posição {i}: ')))
    if i == 0:
        maior = menor = listaNum[i]
    else:
        if listaNum[i] > maior:
            maior = listaNum[i]
        if listaNum[i] < menor:
            menor = listaNum[i]

print('-=' * 30)

print(f'Você digitou os valores {listaNum}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
# Para fazer o mamior valor
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}...', end='')

print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
# para fazer o menor valor
for i, m in enumerate(listaNum):
    if m == menor:
        print(f'{i}...', end='')


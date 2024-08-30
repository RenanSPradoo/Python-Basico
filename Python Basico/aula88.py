valores = []

while True:

    valores.append(int(input('Digite um valor: ')))

    r = str(input('Deseja continuar [S/N]: ')).strip().lower()
    if r == 'n':
        break

print('-=' * 30)
# elementos da lista
print(f'Você digitou {len(valores)} elementos')
# ordem decrescente
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
# verificar se tem o 5 na lista
if 5 in valores:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista')
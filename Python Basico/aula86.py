numero = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não vou adicionar!')

    r = input('Deseja continuar [S/N]: ').strip().lower()
    if r == 'n':  
        break

print('-=' * 50)

numero.sort()
print(f'Você digitou os valores {numero}')

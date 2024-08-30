lista = []

while True:
    lista.append(int(input('Digite um numero: ')))

    r = str(input('Deseja continuar [S/N]: ')).strip().lower()
    if r == 'n':
        break

print('-=' * 30)

print(f'A lista completa é {lista}')

pares = [n for n in lista if n % 2 == 0]  
print(f'A lista com os valores pares é: {pares}')

impares = [n for n in lista if n % 2 != 0]
print(f'A lista com os valores ímpares é: {impares}')
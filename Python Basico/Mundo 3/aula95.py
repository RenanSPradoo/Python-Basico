matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somaColuna = 0

# Preenchimento da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))
         
print('-=' * 30)

# Impressão da matriz e soma dos valores pares
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {soma}')

# Soma dos valores da terceira coluna
for linha in range(0, 3):
    somaColuna += matriz[linha][2]  # Corrigido para acessar a matriz corretamente
print(f'A soma dos valores da terceira coluna é: {somaColuna}')

# Encontrando o maior valor da segunda linha
maior = matriz[1][0]
for coluna in range(1, 3):  # Começa do segundo elemento, pois já inicializamos com o primeiro
    if matriz[1][coluna] > maior: 
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')

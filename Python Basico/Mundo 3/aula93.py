
num = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o  {i} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=' * 30)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitador foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

"""
# Inicializa uma lista com duas sublistas vazias
num = [[], []]

# Inicializa a variável valor com 0
valor = 0

# Inicia um loop que vai de 1 até 7 (inclusive)
for i in range(1, 8):
    # Solicita ao usuário que digite um valor e converte a entrada para um inteiro
    valor = int(input(f'Digite o {i} valor: '))
    
    # Verifica se o valor é par (o resto da divisão por 2 é 0)
    if valor % 2 == 0:
        # Se for par, adiciona o valor à primeira sublista (num[0])
        num[0].append(valor)
    else:
        # Se for ímpar, adiciona o valor à segunda sublista (num[1])
        num[1].append(valor)

# Imprime uma linha de separação para melhor visualização
print('-=' * 30)

# Exibe os valores pares armazenados na primeira sublista
print(f'Os valores pares digitados foram: {num[0]}')

# Exibe os valores ímpares armazenados na segunda sublista
print(f'Os valores ímpares digitados foram: {num[1]}')

"""
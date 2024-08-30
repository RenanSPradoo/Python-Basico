numero = 0
soma = 0
quant = 0

while True:
    numero = int(input('Digite um numero (ou 999 para parar): '))
    if numero == 999:
        break
    soma += numero
    quant += 1

print()
print(f'A quantidade de números digitados foi {quant}')
print(f'A soma dos números digitados é {soma}')

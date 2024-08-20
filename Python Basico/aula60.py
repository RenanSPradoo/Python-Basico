
pessoa = 1
peso = 0
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {pessoa} pessoa: '))
        
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\n')         
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')

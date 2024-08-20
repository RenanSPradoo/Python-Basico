somaIdade = 0
mediaIdade = 0
maioridadeHomem = 0
nomeVelho = ''
totalMulher = 0

for p in range(1, 5):
    print(f'---- {p}° pessoas ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade

    if p == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1

mediaIdade = somaIdade / 4

print()
print(f'A média de idade do grupo é de {mediaIdade} anos. ')
print(f'O homem mais velho tem {maioridadeHomem} anos e se chama {nomeVelho}. ')
print(f'Ao total são {totalMulher} mulheres com menos de 20 anos. ')
print()

from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nacimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <= 25:
    print('Classificação SENIOR')
else:
    print('Classificado MASTER')
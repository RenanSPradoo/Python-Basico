aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno['Nome']}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'RECUPERAÇÂO'
else:
    aluno['Situação'] = 'REPROVADO'

print('-=' * 30)

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')

if media >= 5 and media < 7:
    print('O aluno está de RECUPERAÇÃO.')

elif media < 5:
    print('Aluno está REPROVADO.')

elif media >= 7:
    print('Aluno APROVADO!')
pessoa = dict()
galera = list()
soma = media = 0 

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo : [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'S':
        break

print('-=' * 30)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.') 
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print('C) As mulheres cadsatradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end='')
print()
print(f'D) lista de pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
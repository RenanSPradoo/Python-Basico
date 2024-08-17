# nome = str(input('Qual é seu nome: '))
# if nome == 'Renan':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print(f'Bom dia, {nome}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(media)) 

if media >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim. Estude mais!')
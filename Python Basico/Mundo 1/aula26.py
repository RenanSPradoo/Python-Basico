nome = str(input('Digite seu nome completo: ')).strip() # strip vai eliminas os espaços da frase
print('Analisando o seu nome...')

print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #Cound tira os espaços do meio da frase
# print('Seu nome tem ao todo {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
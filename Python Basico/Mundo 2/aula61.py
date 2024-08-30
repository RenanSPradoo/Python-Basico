frase = str(input('Digite um frase: ')).strip().upper() #eliminou espaços, jogou para maiuscula
palavras = frase.split() #separou em uma lista
junto = ''.join(palavras) #juntou tudo em uma string só
# inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1): #fez o inverso da palavra
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')





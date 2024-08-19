numero = int(input('Digite um numero inteiro: '))
print()
print('Escolha qual será a base de conversão: ')
print('[1] para Binário')
print('[2] para Octal')
print('[3] para Hexadecimal')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\n{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == 2:
    print(f'\n{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == 3:
    print(f'\n{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('\nOpção invalida. Tente novamente! ')
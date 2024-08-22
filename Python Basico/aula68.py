soma = 0
cont = 0
numero = 0 #numero = cont = soma = 0 (INCLUI TODOS VALENDO 0)

digito = int(input('Digite um numero [999 para PARAR]: '))
while digito != 999:
    soma += digito
    cont += 1
    digito = int(input('Digite um numero [999 para PARAR]: '))
print(f'Você digitou {cont} numeros, e a soma entre eles foi {soma}')
    




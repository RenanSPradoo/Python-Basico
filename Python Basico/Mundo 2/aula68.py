soma = 0
cont = 0
numero = 0 #numero = cont = soma = 0 (INCLUI TODOS VALENDO 0)

digito = int(input('Digite um numero [999 para PARAR]: '))
while digito != 999:
    soma += digito
    cont += 1
    digito = int(input('Digite um numero [999 para PARAR]: '))
print(f'Você digitou {cont} numeros, e a soma entre eles foi {soma}')
# Esse codigo faz um looping e quando colocar o valor de 999 ele ira parar por conta do Break que sai função While
n = s = 0
# Vai fazer a soma de todos os numeros e quando digitar 999 vai para.
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break #Sai do while.
    s += n
print(f'A soma vale {s}')

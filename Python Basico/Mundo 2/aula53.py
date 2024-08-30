# for c in range(0, 7, 2): #Dessa maneira com o 2 no final ele vai pular de 2 em 2.
#     print(c)
# print('FIM!')

# for c in range(0, 7): #vai contar de 0 a 6
#     print(c)
# print('FIM!')


# for c in range(1, 7): #vai contar de 1 a 6
#     print(c)
# print('FIM!')

# n = int(input('Digite um numero: '))
# for c in range(0, n+1):
#     print(c)
# print('FIM!')

# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM') # esse print está fora do for (Vai sair sempre essa mensagem)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
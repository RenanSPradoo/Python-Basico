"""
num = [2, 5, 9, 1]
num[2] = 3 # o valor 3 vai entrar no lugar no 9
num[4] = 7 # vai dar erro porque não pode adicionar
num.append(7) #Vai adicinar um numero na lista
num.sort() # Vai organizar os codigos
num.sort(reverse=True) #Vai invertes os codigos
num.insert(2, 2) #Vai pegar o 3 e jogar para frente e adionar o 2 no lugar no 3
if 4 in num:
    num.remove(4) # ele procura no inicio da lista e elimina o primeiro numero
else:
    print('Não achei o numero 4')
num.pop() #Elimita o valor 1
num.pop(2) #O numero volta e retira outro
print(f'Essa lista tem {len(num)} elementos') #Vai mostrar quantos elementos tem

print(num)
"""



"""
valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# for valor in valores:
#     print(f'{valor}...', end='')

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')
print('Cheguei no final da lista ')
"""


"""
# O PYTHON ELE IGUALA UMA LISTA NA OUTRA FAZ UMA LIGAÇÃO
a = [2, 3, 4, 7]
b = a[:] #Vai pegar todos os valores de A e jogar em B (UMA COPIA)
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
"""
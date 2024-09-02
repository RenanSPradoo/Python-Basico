"""
pessoas = [['Pedro', 25], ['Maria', 19], ['Joao', 32]]

print(pessoas[0][0]) #Vai pegar a primeira lista, e pegar o nome 0 da lista (que será PEDRO)
print(pessoas[1][1]) #mesma função porem vai sar (19)
print(pessoas[2][0]) # vai escrever (JOAO)
print(pessoas[1]) #Vai aparecer o bloco completo
"""

"""
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) #Vai sair o mesmo resultado porque está dando uma ligação de 2 estruturas

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
"""

"""
galera = [['Joao', 19], ['Ana', 33], ['Joaqui', 13], ['Maria', 45]]
for i in galera:  # Passa por cada pessoa em 'galera' e coloca na variável 'i'
    print(f'{i[0]} tem {i[1]} anos de idade. ')  # Exibe o nome da pessoa
"""

galera = list()
dado = list()
totalMaior = totalMenor = 0

for cont in range(0, 3):

    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é o maior de idade')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é o menor de idade')
        totalMenor += 1

print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade. ')
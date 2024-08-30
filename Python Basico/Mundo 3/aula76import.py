# ()-Tupla []-Lista {}-Dicionario
# TUPLAS SÂO IMUTAVEIS

# lanche = ('Hamburguer', #0
#     'Suco',  #1
#     'Pizza', #2
#     'Pudim',  #3
#     'Batata Frita' #4
# )
#  print(sorted(lanche)) #Vai sair a listagem de alimento ordenados
#  print(lanche) #Vai sair sem ordenar.

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}') # Esse for ele mostra a posição que está a tupla

#  for pos, comida in enumerate(lanche): 
#     print(f'Eu vou comer {comida} na posição {pos}')  # A mesma coisa que o for de cima ^

#  for comida in lanche:
#      print(f'Eu vou comer {comida}') #Esse for não consegue saber a posição, apenas falar a frase

# print('Comi pra caramba!')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b #Vai juntar as 2 tuplas em apenas 1 sem somar // Se trocar para b + a muda os valores
# print(c)
# print(c.count) #Vai mostrar quantas vezes o numero aparece por ex se for (5) aparece 2x
# print(c.index(8)) #Vai aparecer a onde está o 8 em qual posição

pessoa = ('Renan', 22, 'M', 100.99)
del(pessoa) #del apaga da memoria não vai ter mais essa tupla
print(pessoa) #Em tuplas pode mistrurar str com numeros.
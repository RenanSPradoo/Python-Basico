from random import choice #Choice seria para sortear um nome

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
# [] isso aqui seria uma lista.
alunos = [nome1, nome2, nome3, nome4]
escolhido = choice(alunos)

print('O aluno escolhido foi {}'.format(escolhido))
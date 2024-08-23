"""def mostrarLinha(): # ele chama a funcão sempre para executar as linhas, ele só é lido quando chama no codigo.
    print('----------------------------------------------')
    
mostrarLinha()
print(' Sistema de aluno ')
mostrarLinha()
mostrarLinha()
print(' Cadastro de Funcionarios ')
mostrarLinha()
mostrarLinha()
print(' ERRO DE SISTEMA ')
mostrarLinha()"""

"""def lin():
    print('-=' * 30)

lin()
print(' CURSO EM VIDEO ')
print(' APRENDA PYTHON ')
print(' RENAN PRADO ')
lin()"""

"""def mensagem(msg):
    print('----------------------------------------------')
    print(msg)
    print('----------------------------------------------')
mensagem('Sistema de Alunos')"""

"""def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)
        
titulo('Curso em video')
titulo('Aprenda Python')
titulo('Gustava Guanaraba')"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa principal
soma(b = 4, a = 5)
soma(7 ,2) #Seria A, B
# soma(3, 9, 5) #Não vai funcionar por que na (def(soma) tem apenas 2 função no inicio do codigo)"""


def contador(* num):
    # print(num) #Dessa forma vai criar uma tupla
    # for valor in num:
    #     print(f'{valor} ', end='')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
def teste(b):
    
    global a #Vai usar o A que vale 5, e vai usar como Todo e vai perder o valor 5
    b += 4
    c = 2
    print(f'A dentro vale{a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')   

a = 5 #perde o valor 5 
teste(a)
print(f'A fora vale {a}')
#! ^_________ESCOPO GLOBAL __________ ^
# EXEMPLOS:
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}') #4 // escopo local

n1 = 2 #escopo global
funcao()
print(f'N1 fora vale {n1}') #2 
#!__________FINALIZANDO ESCOPO__________

#? _______COMO UTILIZAR RETURN________
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1},{r2} e {r3}.')
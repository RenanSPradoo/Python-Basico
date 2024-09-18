import uteis115 #Vai importar outra pasta de codigo dentro do meu para ficar um CLEAN code
# from uteis115 import fatorial, dobro || dessa maneira fica mais facil pois não precisa usar o uteis115.(...) || Porem o python n recomenda por bugs

num = int(input('Digite um valor: '))
fat = uteis115.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis115.dobro(num)}')


"""
from uteis importe fatorial
from math import sqrt
from datetime import datetime
from random import randint

from (MODULO) import (FUNÇÂO)
"""
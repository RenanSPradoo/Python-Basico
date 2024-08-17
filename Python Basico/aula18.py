#  Para importar biblioteca 
# import bebida # Vai incluir diretamente todas as bebidas que tiver
# from doce import (PUDIM) Vai incluir apenas o pudim e não todos os doces

# import math IMPORTA TODAS AS MATEMATICAS
# from math import sqrt #Importe a biblioteca de mateica porem apenas Raiz Quadrada

from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.0f} '.format(num, raiz))


# Biblioteca de Math tem oque:
"""
ceil (arredonda para cima)
floor (arredonda para baixo)
trunc (vai eliminar da virgula para frente, sem arredondamento)
pow (potencia semelhante ao **)
sqrt (calcula raiz quadrada)
factorial (calcula fatorial)
"""
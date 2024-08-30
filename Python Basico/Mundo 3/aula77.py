# Cria a tupla com os números de zero até vinte por extenso
numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte'
)

while True:
    # Solicita ao usuário que insira um número entre 0 e 20
    numero = int(input('Digite um número entre 0 e 20 (ou um número fora desse intervalo para sair): '))
    
    # Verifica se o número está no intervalo válido
    if 0 <= numero <= 20:
        print(f'\nVocê digitou o número {numeros_extenso[numero]}.', end='' )
    else:
        print('\nNúmero fora do intervalo. Encerrando o programa.')
        break  # Sai do loop e termina o programa

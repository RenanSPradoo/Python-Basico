def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um numero valido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um numero valido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

num1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor digitado foi {num1} e o valor real foi {n2}')
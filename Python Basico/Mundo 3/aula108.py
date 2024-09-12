from time import sleep

def maior(num): #! esse vai receber varios parametros ou nenhum e vai desempacotar
    cont = maior = 0
    print('-=' * 30)
    print(f'\nAnalisando os valores passados...')

    for valor in num:
        print(f'{valor}', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O mairo valor informado foi {maior}')

#! PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
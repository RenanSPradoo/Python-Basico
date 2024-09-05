ficha = list()

while True:

    media = (nota1 + nota2) / 2

    nome = str('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    ficha.append([nome, [nota1, nota2], media]) #Lista composta com dados do aluno
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn': #Tentar com == em vez de in 
        break  

print('-=' * 30)
print(f'{f'No.':<4}{'Nome':<10}{'Media':>8}')
print('-' * 26) 

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<< Volte sempre >>>>')
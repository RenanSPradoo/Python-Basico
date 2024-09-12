def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m². ')

print('Controle de Terrenos')
print('-=' * 20)

l = float(input('Largura em (m): '))
c = float(input('Comprimento (m): '))
area = (l , c)
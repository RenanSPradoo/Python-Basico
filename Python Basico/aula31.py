frase = str(input('Digite uma frase: ')).upper().strip
print('A letra A aparece {} na frase'.format(frase.count('A'))) #count vai contar quantos A tem na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #findi vai mostrar a posição da letra A
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #rfindi a ultima letra está no 7 lugar
from datetime import date

atual = date.today().year
totalMaior = 0
totalMenor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}° pessoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print(f'Ao todo tivemos {totalMaior} pessoas maiores de idade.')
print(f'E também tivemos {totalMenor} pessoas menores de idade.')
peso = float(input('Qual é o seu peso? (KG): '))
altura = float(input('Qual é sua altura (M): '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoal é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif imc >= 18.5 and imc < 25:
    print('PARABENS está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('você está SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA')
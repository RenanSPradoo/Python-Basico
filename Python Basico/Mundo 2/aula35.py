# Condição simples sem o (ELSE)

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar com multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')    

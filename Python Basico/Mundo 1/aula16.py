dias_alugados = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias_alugados * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
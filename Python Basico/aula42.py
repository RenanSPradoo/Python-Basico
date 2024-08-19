valor_casa = float(input('Qual o valor da casa R$ '))
salario = float(input('Qual o seu salario R$ '))
anos = int(input('Em quantos anos vai pagar? '))

minimo = salario * 30 / 100
prestacao = valor_casa / (anos * 12)
print(f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print('\nEmprestimo pode ser CONCEDIDO!')
else:
    print('\nEmprestimo NEGADO!')
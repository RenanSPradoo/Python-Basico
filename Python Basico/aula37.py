distancia = float(input('Qual é a distancia da sua viagem? '))
print(f'Você está prester a começar uma viagem de {distancia}KM!')

# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 / (MANEIRA MAIS SIMPLES DE FAZER)

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
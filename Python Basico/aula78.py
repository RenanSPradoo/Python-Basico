times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 
        'Cruseiro', 'Flamento', 'Vasco', 'Chapecoense',
        'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
        'São Paulo', 'Fluminence', 'Sport-Recife',
        'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
        'Atletico-GO' 
        )

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times: {times[:5]}') #[0:5] também da na mesma
print('-=' * 15)
print(f'Os ultimos 4 colocados: {times[16:20]}') #[-4] da na mesma
print('-=' * 15)
print(f'Times em ordem alfabeticas: {sorted(times)}') #Sorted não muda ordem da tupla o idela seria esse.
print('-=' * 15)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição')
print('-=' * 15)


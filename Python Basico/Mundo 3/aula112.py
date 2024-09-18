def ficha(jog = 'Desconhecido' , gol = 0):
    return f'O jogador {jog} fez {gol} gol(s) no campeonado. '

n = str(input('Nome do jogador: '))
g = str(input('Numero de GOLS: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)
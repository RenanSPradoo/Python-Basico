"""
Palavra usada (Curso em Video Python)
"""

# Fatiamento
# frase[9] = ele vai identificar apenas o caracter 9(que seria o 10 caracter)
# frase[9:13] = ele começa no nove e vai até o 13(sempre precisa colocar 1 a mais para não excluir a palavra)
# frase[9:21:2] = ele vai começar no nove e vai para no 21 (e vai pular de 2 em 2)
# frase[:5] = que seria vai começar do 0 até a str 5
# frase[15:] = vai começar do 15 até o final
# frase[9::3] = vai começar no 9 e vai até o final já que no meio dos 2 pontos está vazio (e vai pular de 3 em 3)

# Analise
# len(frase) = comprimento da frase (Curso em Video Python vai de 0 a 21)
# frase.count('o') = contar quantas letra (o) tem na frase.
# frase.count('o',0,13) = Conta quantas vezes a letra 'o' aparece na string 'frase', mas só olha até o índice 13 (não inclui o índice 13).
# frase.find('deo') = vai pegar todas as palavras que tem d/e/o
# 'Curso' in frase = existe curso em frase? (True)

# Transformação
# frase.replace('Python','Android') = ele iria substituir o Python por (android)
# frase.upper() = oque for maiosculo ele mantem, e oque for em minusculo fica em maiuscula
# frase.lower() = ao contrario do upper
# frase.capitalize() = ele vai jogar todas as caracteres em minusculo e vai ficar apenas a primeira letra em maiuscula
# frase.title() = Ele vai analisar quantas palavras tem essa str
# frase.strip() = vai remover os primeiros espaços vazios e os ultimos (se tiver espaço no meio vai manter)
# frase.rstrip() = se tiver o r na frente ele vai remover apenas os espaços que está vaios no final da frase
# frase.lstrip() = quando tem L na frente da frase significa LEFT que seria remover os espaços apenas da esquerda

# Divisão
# frase.split() = cada palavra colocada dentro do split é coloca dentro de outra lista (0,1,2,3,4)(0,1)(0,1,2,3,4,5)(0,1,2,3)

# Junção
# '-'.join(frase) = vai juntar todos os elementos de frase usando (-)
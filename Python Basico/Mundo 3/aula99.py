pessoas = {'Nome':'Renan',
           'Sexo':'M',
           'idade':22}

# pessoas['Peso'] = 98.5
# Vai adicionar a varial PESO no final do dict

# pessoas['Nome'] = 'Beto'
# Vai trocar o nome de 'RENAN' para 'BETO'

# del pessoas['Sexo']
# Vai apagar o dict (SEXO)

"""EXEMPLOS DE COMO FAZER ABAIXO: """
# print(pessoas['Nome']) Vai mostrar Renan
# print(pessoas['Sexo']) vai mostrar M
# print(pessoas['Idade']) vai mostrar 22
# print(f'O {pessoas['Nome']} tem {pessoas['Idade']} anos') #Como fazer de forma FORMATADA
# print(pessoas.keys()) #Vai mostrar (NOME, SEXO, Idade) (CHAVES)
# print(pessoas.values()) #Vai mostrar (GUSTAVO, M, 22) (VALORES)
# print(pessoas.items()) #Vai mostrar (nome renan) (sexo M) (idade 22) que seria uma (LISTA dentro de 3 TUPLAS)

for k in pessoas.keys():
    print(k)
#vai mostrar NOME SEXO IDADE

for k in pessoas.values():
    print(k)
#vai mostrar RENAN M 22

for k, v in pessoas.items():
    print(f'{k} = {v}')
# Vai mostrar nome = Renan, sexo = M, idade = 22


"""COMO CRIAR UM DICIONARIO DENTRO DE UMA LISTA ABAIXO: """
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'Sigla':'RJ'}
estado2 = {'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) #Vai mostrar a str do estado1 
print(estado2) #vai mostrar a str do estado2 
print(brasil) #Vai mostrar ambos em forma de dicionario 
print(brasil[0]) #Vai mostrar o primeiro (uf':'Rio de Janeiro', 'Sigla':'RJ)
print(brasil[1]) #Vai mostrar o primeiro (uf':'São Paulo','Sigla':'SP)
print(brasil[0]['uf']) #Vai mostrar Rio de Janeiro
print(brasil[1]['Sigla']) #Vai mostrar SP

print('-=' * 30)

estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #O dicionario não pode fazer fatiamento [:], o .copy() seria 
# print(brasil)
for e in brasil:
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}')
    for v in e.value():
        print(v, end=' ')
    print()
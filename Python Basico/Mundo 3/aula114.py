def notas(*n, sit=False): #Esse (*n) significa que vai ter varios numeros 
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)

    if sit:
        if r['Media'] > 7:
            r['Situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)

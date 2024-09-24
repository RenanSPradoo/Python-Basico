try: #TENTE (OPERAÇÂO)
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro: # Se der o problema(FALHOU
    print(f'Problema encontrado foi {erro.__class__}') #! Imprime o tipo da exceção (exemplo: ValueError, TypeError, etc.)
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir esse numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')#Vai mostrar a causa do erro
else:   #Se der certo(DEU CERTO)
    print(f'O resultado é {r}')
finally: #Certo ou errado ele aparece no final do codigo.(OPCIONAL)
    print(f'Volte sempre, Muito obrigado!')
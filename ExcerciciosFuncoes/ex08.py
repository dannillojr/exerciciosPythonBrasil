'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def qtd_digitos(num):
    qtd_digitos = len(str(num))
    return qtd_digitos

print(qtd_digitos(10000))

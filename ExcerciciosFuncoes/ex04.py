'''
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
se seu argumento for zero ou negativo.
'''

def verificar_pos_neg(x):

    if x > 0:
        return "P"
    else:
        return 'N'

print(verificar_pos_neg(10))
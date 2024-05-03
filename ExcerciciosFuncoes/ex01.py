'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba 
um valor n inteiro e imprima até a n-ésima linha.
'''
def numero_duplicado(n):
    for n in range(n+1):
        print(f'{str(n)*n}')

numero_duplicado(10)
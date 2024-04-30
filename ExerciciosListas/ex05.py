'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
'''



total_numeros = []
numeros_par = []
numeros_impar = []

for i in range(1, 10):

    numeros = int(input('digite numeros inteiros: '))
    total_numeros.append(numeros)

for numero in total_numeros:

    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)
print('')

print('Total numeros 👇')
for n in total_numeros:
    print(f'{n}', end=' ')

print('')

print('Numeros pares 👇')
for par in numeros_par:
    print(par, end=' ')

print(' ')

print('Numeros impares 👇')
for impar in numeros_impar:
    print(impar, end=' ')
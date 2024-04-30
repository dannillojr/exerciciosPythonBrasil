#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n = int(input('N termos: '))

numerador = 1
soma = 0

for denominador in range(1, n+1):

    resultado = numerador / denominador

    soma += resultado

    print(f'1 / {denominador} = {resultado:.2f}')

print(f'Soma resultado de n termos: {soma:.2f}')
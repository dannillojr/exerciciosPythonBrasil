'''
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = [1,2,3,4,5,6,7,8,9,10]

quadrado = 0
soma = 0
for n in numeros:
    quadrado = n ** 2
    soma += quadrado
print(soma)
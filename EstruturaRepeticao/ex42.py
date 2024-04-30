'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''

contador0_25 = 0
contador26_50 = 0
contador51_75 = 0
contador76_100 = 0

while True:
    entrada = int(input('Digite um numero inteiro: '))

    if entrada < 0:
        break
    else:
        if entrada > 0 and entrada <= 25:
            contador0_25 +=1

        elif entrada > 25 and entrada <=50:
            contador26_50 +=1

        elif entrada > 50 and entrada <= 75:
            contador51_75 += 1

        elif entrada > 75 and entrada <=100:
            contador76_100 +=1

print(contador0_25)
print(contador26_50)
print(contador51_75)
print(contador76_100)

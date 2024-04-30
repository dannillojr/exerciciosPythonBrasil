# '''
# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.
# '''
qtd_numeros_pare = 0
qtd_numeros_impares = 0

for i in range(10):
    i+=1
    numeros = int(input(f'Digite o {i} numero: '))

    if numeros % 2 == 0:
        qtd_numeros_pare += 1
    else:
        qtd_numeros_impares += 1

print(f'Foi digitado {qtd_numeros_pare} numeros pares...')
print(f'Foi digitado {qtd_numeros_impares} numeros impares...')
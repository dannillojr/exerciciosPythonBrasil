# '''
# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# '''
numeros = []

while True:
    numero = int(input('Digite numeros inteiros : '))
    if numero > 1000 or numero < 0:
        print('Numeros menores que 0 ou maiores que 1000 não são permitidos')
        break
    else:
        numeros.append(numero)

print(numeros)

maior = numeros[0]
menor = numeros[0]
soma = 0


for item in numeros:
    
    soma = soma + item

    if item > maior:
        maior = item

    if item < menor:
        menor = numero

print(f'A soma dos numeros digitados é {soma}')       
print(f'O maior numero entre os digitados é {maior}')     
print(f'O menor numero entre os digitados é {menor}')     



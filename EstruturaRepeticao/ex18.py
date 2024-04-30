numeros = [90,3,7,21,30,4,5,1]

maior = numeros[0]
menor = numeros[0]
soma = 0

for numero in numeros:

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

for valor in numeros:
    soma = soma + valor

print(maior)
print(menor)
print(soma)
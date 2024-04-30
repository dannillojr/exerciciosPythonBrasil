# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo

numero_inteiro1 = input('Digite um numero inteiro: ')
numero_inteiro2 = input('Digite outro numero inteiro: ')
numero_real = input('Digite um numero real: ')

numero_inteiro1 = float(numero_inteiro1)
numero_inteiro2 = float(numero_inteiro1)
numero_real = float(numero_real)

resp1 = (numero_inteiro2 / 2) * (numero_inteiro1 * 2)
resp2 = (numero_inteiro2 * 3) + (numero_real)
resp3 = numero_real ** 3

print()

print(f'o produto do dobro do primeiro com metade do segundo: {resp1}')
print()

print(f'a soma do triplo do primeiro com o terceiro: {resp2}')
print()

print(f'o terceiro elevado ao cubo: {resp3}')
print()

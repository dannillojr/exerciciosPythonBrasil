#C = 5 * ((F-32) / 9).

fahrenheit = input('Valor em graus fahrenheit: ')

celsius = 5 * ((int(fahrenheit) - 32) /9)

print(f'fahrenheit -->> {celsius:.2f}')
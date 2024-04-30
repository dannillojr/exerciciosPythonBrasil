numero = int(input('Digite um numero inteiro: '))

resultado = 1

for i in range(numero, 0 , -1):
    resultado = resultado * i
print(resultado)
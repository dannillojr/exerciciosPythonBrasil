
numeros = []
contador = 0

while True:

    contador += 1
    n1 = int(input('Digite um valor: '))
    numeros.append(n1)

    if contador == 3:
        break

    
numeros.sort(reverse=True)
print(numeros)

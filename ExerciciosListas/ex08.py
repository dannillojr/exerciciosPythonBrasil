'''
Faça um Programa que peça a idade e a altura de 5 pessoas, 

armazene cada informação no seu respectivo vetor. 

Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idades = []
alturas = []

for i in range(1,3):
    idade = int(input(f'idade {i}ª pessoa: '))
    altura = float(input(f'altura {i}ª pessoa: '))

    idades.append(idade)
    alturas.append(altura)

    print(' ')

for i in reversed(idades):
    print(i)

for x in reversed(alturas):
    print(x)



# print(idades)
# print(alturas)
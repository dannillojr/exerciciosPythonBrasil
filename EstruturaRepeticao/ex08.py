# '''
# Faça um programa que leia 5 números e informe a soma e a média dos números.

# '''
soma = 0
media = 0

for i in range(4):

    numeros = int(input(f'Digite {i+1}º valor:'))
    soma +=numeros

media = soma / (i+1)

print(soma)
print(media)


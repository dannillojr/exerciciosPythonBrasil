# '''
# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.
# '''

n = int(input('N termos: '))

denimonador = 1
resultado = 0

for i in range(1, n+1):

    divisoes = i/denimonador
    resultado += divisoes
    denimonador += 2

print(f'{resultado:.2f}') 



# '''
# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no 
# intervalo compreendido por eles.
# '''

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 <= numero2:
    
    for i in range(numero1, numero2 +1):
        print(i, end=' ')
else:
    print('Numero 1 tem que ser menor que numero 2')
    

    




# '''
# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no 
# intervalo compreendido por eles.


# Altere o programa para mostrar no final a soma dos números.

# '''

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
soma = 0

if numero1 <= numero2:
    
    for i in range(numero1, numero2 +1):
        soma += i
        print(i)
    
else:
    print('Numero 1 tem que ser menor que numero 2')
    
print(f'A somas do numeors do intervalo é : {soma}')
    




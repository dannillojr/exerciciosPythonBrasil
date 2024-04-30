# '''
# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# '''

numero = int(input('Digite um numero: '))

cont = 0

for n in range(1, numero): 
    
    if n > 1:
        primo = True
        
        for i in range(2, n):
            cont += 1
            if n % i == 0:
                primo = False
                break
                
        if primo :
            print(f'{n} - é primo: ')
            
        else:
            print(f'{n} - Não é primo..')
            
    else:
        print(f'{n} Não é primo numeros primos são maiores que 1..')

print(f'Foram realizada {cont} divisões para encontrar os numeros primos')




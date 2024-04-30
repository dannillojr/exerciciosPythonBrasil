numero = int(input('Digite um numero: '))

if numero > 1:
    
    primo = True
    divisores = []
    
    for i in range(2, numero):
        
        if numero % i == 0:
            primo = False
            divisores.append(i)
            

    if primo :
        print(f'{numero} é primo: ')
        
    else:
        print(f'{numero} Não é primo..')
        print(f'É divisivel por {divisores}')
        
else:
     print(f'{numero} Não é primo numeros primos são maiores que 1..')

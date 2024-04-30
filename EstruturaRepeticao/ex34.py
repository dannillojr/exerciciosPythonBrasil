numero = int(input('Digite um numero inteiro: '))

if numero > 1:
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f'{numero} É primo')
    else:
        print(f'{numero} Não é primo')

else:
    print('Não é primo')
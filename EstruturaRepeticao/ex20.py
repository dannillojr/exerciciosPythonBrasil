
while True:
    fatoriais = 1

    numero = int(input('Digite um numero para calculo fatorial: '))

    if numero > 16 or numero < 0:

        print('Numeros menores que 0(zero) ou maiores que 16 não são permitidos')
        break

    else: 

        for i in range(numero, 0, -1):
            fatoriais *= i
            
    print(fatoriais)

    encerrar = input('Deseja continuar [C] ou encerrar [E]: ')

    if encerrar.upper() == 'E':
        print('Encerrado ...')
        break
    else:
        print('Continuando...')
        continue


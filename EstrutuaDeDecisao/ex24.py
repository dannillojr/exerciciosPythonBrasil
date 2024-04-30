'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.

'''

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

operacao = input('Qual operação deseja realizar [+] - [-] - [x] - [/]: ')

try:
    if operacao == '+':
        soma = n1 + n2
        if soma % 2 == 0:
            par_impar = 'par'
        else:
            par_impar = 'impar'

        if soma > 0 :
            neg_posit = 'positivo'
        else:
            neg_posit = 'negativo'

        if soma == round(soma):
            int_dec = 'inteiro'
        else:
            int_dec= 'decimal'
        
        print(f'o rusultado de {n1} {operacao} {n2} é: {soma}')
        print(f'{soma} é um numero: {par_impar} - {neg_posit} - {int_dec}')

    elif operacao == '-':
        sub = n1 - n2

        if sub % 2 == 0:
            par_impar = 'par'
        else:
            par_impar = 'impar'

        if sub > 0 :
            neg_posit = 'positivo'
        else:
            neg_posit = 'negativo'

        if sub == round(sub):
            int_dec = 'inteiro'
        else:
            int_dec= 'decimal'
            
            print(f'o rusultado de {n1} {operacao} {n2} é: {sub}')
            print(f'{sub} é um numero: {par_impar} - {neg_posit} - {int_dec}')

    elif operacao == 'x':
        mult = n1 * n2
        if mult % 2 == 0:
            par_impar = 'par'
        else:
            par_impar = 'impar'

        if mult > 0 :
            neg_posit = 'positivo'
        else:
            neg_posit = 'negativo'

        if mult == round(mult):
            int_dec = 'inteiro'
        else:
            int_dec= 'decimal'
            
            print(f'o rusultado de {n1} {operacao} {n2} é: {mult}')
            print(f'{mult} é um numero: {par_impar} - {neg_posit} - {int_dec}')

    elif operacao == '/':
        div = n1 / n2
        if div % 2 == 0:
            par_impar = 'par'
        else:
            par_impar = 'impar'

        if div > 0 :
            neg_posit = 'positivo'
        else:
            neg_posit = 'negativo'

        if div == round(div):
            int_dec = 'inteiro'
        else:
            int_dec= 'decimal'
            
            print(f'o rusultado de {n1} {operacao} {n2} é: {div}')
            print(f'{div} é um numero: {par_impar} - {neg_posit} - {int_dec}')
    else:
        print('Digite uma operação valida [+] - [-] - [x] - [/]: ')
except ZeroDivisionError:
    print('Ta tentando dividir alguma coisa por zero ai arrombado reinicie')




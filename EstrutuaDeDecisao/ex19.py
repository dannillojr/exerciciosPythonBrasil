'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 

326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

'''

numero = int(input('Digite um numero inteiro menos que 1000: '))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

resultado = ''

#verificador texto centenas
if centenas > 0 :
    if centenas == 1:
        resultado += '1 centena'
    else:
        resultado += f'{centenas} centenas'

#verificador texto dezenas
if dezenas > 0:
    if resultado:
        resultado+= ', '
    if dezenas == 1:
        resultado += '1 dezena'
    else:
        resultado += f'{dezenas} dezenas'

#verificador texto unidades
if unidades > 0:
    if resultado:
        if not dezenas and centenas:
            resultado += ' e '
        else:
            resultado += ' e ' 

    if unidades == 1:
        resultado += '1 unidade'
    else:
        resultado += f'{unidades} unidades'

print(resultado)



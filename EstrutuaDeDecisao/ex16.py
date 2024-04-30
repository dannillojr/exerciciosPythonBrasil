'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero,
a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

'''

a = int(input('valor 1: '))

if a == 0:

    print('A equação não é do segundo grau. Encerrando o programa.')

else:

    b = int(input('valor 2: '))
    c = int(input('valor 3: '))

    delta = b ** 2 - 4 * a * c

    if delta < 0 :

        print("A equação não possui raízes reais. Encerrando o programa.")

    elif delta == 0:

        raiz = -b / (2 * a)
        print(f'A equação possui um raiz : {raiz:.2f}')

    else:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f'A equação possui duas raizes: {raiz1:.2f}, {raiz2:.2f}')
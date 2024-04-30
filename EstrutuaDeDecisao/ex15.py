'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. Indique, 
caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado1 = float(input('Digite um lado do triangulo: '))
lado2 = float(input('Digite um lado do triangulo: '))
lado3 = float(input('Digite um lado do triangulo: '))

def verifica_triangulo(a, b, c):

    if a < b + c and b < a + c and c < a + b:
        return True
    else: 
        return False
    
if verifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        print('é um triangulo: Equilatero')

    elif lado1 != lado2 != lado3:
        print('é um triangulo: Escaleno')
        
    elif lado1 == lado2 !=lado3:
        print('é um triangulo: Isósceles')
else:
    print('Não é um triangulo')

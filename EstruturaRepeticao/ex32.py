# '''
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120
# '''

numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero > 1:
    fatorial = 1

    print(f"Fatorial de: {numero}")
    print(f"{numero}! = ", end="")

    while numero > 1:
        fatorial *= numero

        print(f"{numero} . ", end="")

        numero -= 1
        
    print(f"1 = {fatorial}")
else:
    print("Não é possível calcular o fatorial de um número negativo.")


'''
 Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

'''

nota1 = float(input('NOTA 1: '))
nota2 = float(input('NOTA 2: '))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print(nota1, nota2, "A")

elif media >= 7.5 and media < 9:
    print(nota1, nota2, "B")

elif media >= 6 and media < 7.5:
    print(nota1, nota2, "C")

elif media >= 4 and media < 6:
    print(nota1, nota2, "D")

elif media < 4:
    print(nota1, nota2, "E")
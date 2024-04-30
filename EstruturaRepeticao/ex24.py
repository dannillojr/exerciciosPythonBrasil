'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

qtd_notas = int(input('Quantas notas irá calcular: '))

nota = 0

for i in range(qtd_notas):
    i += 1
    notas = float(input(f'Digita a {i}ª nota: '))
    nota += notas
    media = nota / qtd_notas
print(media)

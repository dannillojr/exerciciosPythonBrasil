# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# O resultado do atleta será determinado pela média dos cinco valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
# em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
# O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m'''
import os
nome_atletas = []
saltos_atletas = []
medias = []


while True:
    nome_atleta = input('NOME ATLETA: ')

    if nome_atleta == '':
        os.system('cls')
        break
    else:
        nome_atletas.append(nome_atleta)
        saltos_atleta = []
        for s in range(5):
            salto = float(input('SALTO DO ATLETA: '))
            
            saltos_atleta.append(salto)
            
        saltos_atletas.append(saltos_atleta)
        print(' ')

print('')
print(f'{"RESULTADO":-^100}')
print('')

print(F'{'ATLETAS':<10} {'S1':<13} {'S2':<13} {'S3':<13} {'S4':<13} {'S5':<13} {'RESULTADO':<10}')
print('')
for nome, saltos in zip(nome_atletas, saltos_atletas):
    total_por_salto = 0
    print(f'{nome:<10}', end=' ')


    for salto in saltos:
        total_por_salto += salto
        print(f'{salto}{'m':<10}', end=' ')

    media = total_por_salto / 5
    medias.append(media)

    print(f'{media}{'m':<10}')

    print('')

maior_media = 0
nome_maior_media = ''

for i, media in enumerate(medias):

    if media > maior_media:
        maior_media = media
        nome_maior_media = nome_atletas[i]

print(f'Vencedor: {nome_maior_media} com {maior_media}m')


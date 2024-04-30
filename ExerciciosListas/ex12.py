'''
Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = [10,12,14,15,17,9,8,16,17,19]
alturas = [110,120,130,170,100,90,150,130,119,120]

soma_alturas = 0

alunos_mais_13_altura_menor_meria = []

cont = 0

for a in alturas:
    soma_alturas += a

media = soma_alturas / 10

for i, idade in enumerate(idades):
    if idade > 13 and alturas[i] < media:
        cont +=1
print(f'{cont} alunos tem mais que 13 anos e são menores que {media}cm')

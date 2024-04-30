'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 
2 suspeita
3 e 4 cumplice
5 assassino
1 ou 0 inocente
'''

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",

]

cont_sim = 0

for pergunta in perguntas:
    print(pergunta)
    resp = input('[S] se sim [N] se não: ')
    print('')

    if resp.upper() == 'S':
        cont_sim += 1

if cont_sim == 5:
    print(f'{cont_sim} - Assassino')

elif cont_sim == 3 or cont_sim == 4:
    print(f'{cont_sim} - Complice')

elif cont_sim == 2:
    print(f'{cont_sim} - Suspeito')

else:
    print(f'{cont_sim} = Inocente')
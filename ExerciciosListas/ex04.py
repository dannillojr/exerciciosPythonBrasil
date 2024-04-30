'''
]Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

'''

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vogais = ['a', 'e', 'i', 'o', 'u']

for letra in letras:

    for vogal in vogais:
        if letra == vogal:
            letras.remove(letra)

qtd_consoantes = len(letras)

print(f'Foram lidas {qtd_consoantes} consoantes.')

for letra in letras:
    print(letra, end=' ')
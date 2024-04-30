# '''
# Faça um programa que leia 5 números e informe o maior número.
# '''
maior_numero = 0
posicao_maior = 0

for i in range(5):
    numero = int(input(f'Digite o {i+1}º numero: '))

    if maior_numero < numero:
        maior_numero = numero
        posicao_maior = i + 1


print(f'O maior numero entre os digitados é {maior_numero} foi digitado na {posicao_maior}ª pergunta')
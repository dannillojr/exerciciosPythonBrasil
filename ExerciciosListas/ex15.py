'''
Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando 
for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;✅
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;✅
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;✅
Calcule e mostre a soma dos valores;✅
Calcule e mostre a média dos valores;✅
Calcule e mostre a quantidade de valores acima da média calculada;✅
Calcule e mostre a quantidade de valores abaixo de sete;✅
Encerre o programa com uma mensagem;

'''

numeros = []

cont = 0
while True:
    numero = int(input('Digite um numero[-1] para parar: '))

    if numero == -1:
        break   
    else:
        cont += 1
        numeros.append(numero)

soma_numeros = sum(numeros)
media = soma_numeros / len(numeros)

qtd_acima_media = 0
qtd_abaixo_7 = 0

print(f'Foram lidos {cont} numeros')
print('')
print(f'os valores na ordem lado a lado 👇')
for num in numeros:
    print(f'{num}', end=' ')

print('')
print('')
print(f'valores na ordem inversa baixo do outro👇')
for num1 in reversed(numeros):
    print(f'{num1}')

print('')

print(f'A soma dos numeros : {soma_numeros}')
print(f'A media dos numeros: {media}')

print(' ')

for num2 in numeros:
    if num2 > media:
        qtd_acima_media +=1
    if num2 < 7:
        qtd_abaixo_7 +=1
    
print(f'{qtd_acima_media} acima da média calculada...')
print(f'{qtd_abaixo_7} abaixo de 7...')

print('Relatorio finalizado')
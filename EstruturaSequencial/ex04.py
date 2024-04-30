nota_inicial = 0

for i in range(4):
    i += 1
    notas = input(f'Ditie a {i}ª nota: ')
    nota_inicial += int(notas)
    media = nota_inicial / i


print(f'Sua media foi {media}')

if media < 6:
    print('reprovado')
else:
    print('aprovado')

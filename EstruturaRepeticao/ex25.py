# '''
# Faça um programa que peça para n pessoas a sua idade, 
# ao final o programa devera verificar se a média de idade 
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, 
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
# '''
qtd_idades = int(input('Quanta idades irá calcular: '))
print('')
idade = 0 

for i in range(qtd_idades):
    i +=1
    idades = int(input('Qual sua idade: '))
    idade += idades

    media = idade / qtd_idades

    if media > 0 and media < 25:
        classificacao = 'jovens..'

    elif media >= 26 and media < 60:
        classificacao = 'adultos..'

    elif media > 60:
        classificacao = 'idosos..'

print('')
print(f'A media da turma é {media}')
print(f'Com base na media a turma é composta por {classificacao}')
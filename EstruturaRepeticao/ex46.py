# '''
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. 

# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta 
# em seus saltos e depois informe a média dos saltos conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
# Os saltos são informados na ordem da execução, portanto não são ordenados. 
# O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

# '''
nome = input('Nome do atleta: ')

saltos = []
saltos_sem_alteracao = []
maior_salto = 0
menor_salto = 0
soma_saltos_restantes = 0

for pulo in range(1, 6):
    valor_pulo = float(input(f'{pulo}ª salto: '))
    saltos.append(valor_pulo)
    saltos_sem_alteracao.append(valor_pulo)

menor_salto = min(saltos)
maior_salto = max(saltos)

saltos.remove(menor_salto)
saltos.remove(maior_salto)

for salto in saltos:
    soma_saltos_restantes += salto

media = soma_saltos_restantes / len(saltos)  

print('')

print(f'Atleta: {nome}')

print('')

for i, sa in enumerate(saltos_sem_alteracao):
    i+=1
    print(f'{i}ª salto: {sa}m ')

print('')

print(f'Melhor salto: {maior_salto}')
print(f'Pior salto: {menor_salto}')
print(f'Media dos demais saltos conforme a regra: {media}m')

print('')

print('Resultado final:')
print(f'{nome}: {media}m')




# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
# Foram obtidos os seguintes dados:

# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999).

# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidade_maior_indice = None
cidade_menor_indice = None

valor_maior_indice = 0
valor_menor_indice = 0


total_veiculos = 0
total_acidentes_cidade_menor_2000 = 0

contador_menor_2000 = 0
contador_total_cidade = 0

for x in range(1,3):
    
    nome_cidade = input('Digite o nome da cidade: ')
    numero_veiculos = int(input('Quantos veiculos nessa cidade: '))
    numero_acidente = int(input('Digite a quantidade de acidentes registrados com vitimas: '))
    print('')

    contador_total_cidade +=1
    total_veiculos += numero_veiculos


    if numero_acidente > valor_maior_indice:
        valor_maior_indice = numero_acidente
        cidade_maior_indice = nome_cidade

    if numero_acidente < valor_menor_indice or valor_menor_indice == 0:
        valor_menor_indice = numero_acidente
        cidade_menor_indice = nome_cidade
    
    if numero_veiculos < 2000:
        contador_menor_2000 +=1
        total_acidentes_cidade_menor_2000 += numero_acidente

media_veiculos = total_veiculos / contador_total_cidade
media_acidentes_cidade_menor_2000 = total_acidentes_cidade_menor_2000 / contador_menor_2000

print('')
print(f'A cidade com maior indice de acidente é {cidade_maior_indice} com {valor_maior_indice} de acidentes')
print(f'A cidade com menor indice de acidente é {cidade_menor_indice} com {valor_menor_indice} de acidentes')
print(f'A media de veiculo das {contador_total_cidade} cidades juntas é de {media_veiculos} veiculos por cidade')
print(f'A media de acidente das cidades com menor de 2000 habitantes é de {media_acidentes_cidade_menor_2000} por cidade')
        
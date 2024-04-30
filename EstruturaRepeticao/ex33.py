# '''
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver
# um programa que leia as um conjunto indeterminado de temperaturas, 
# e informe ao final a menor e a maior temperaturas informadas, 
# bem como a média das temperaturas.
# '''
temperaturas = [30, 20, 40, 21, 23, 38, 19]

maior_temp = temperaturas[0]
menor_temp = temperaturas[0]
total_temp = 0


for temp in temperaturas:

    total_temp += temp

    if temp > maior_temp:
        maior_temp = temp

    if temp < menor_temp:
        menor_temp = temp
    
    media = total_temp / len(temperaturas)

print(f'A menor temperatura na lista é: {menor_temp}Cº')
print(f'A maior temperatura na lista é: {maior_temp}Cº')
print(f'A media é de : {media:.2f}Cº no geral')
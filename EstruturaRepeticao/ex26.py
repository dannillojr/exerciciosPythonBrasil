# '''
# Numa eleição existem três candidatos. 
# Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
# '''
qtd_votos_c1 = 0
qtd_votos_c2 = 0
qtd_votos_c3 = 0

qtd_eleitores = int(input('Quantas pessoas vão votar: '))

for x in range(qtd_eleitores):
    x+=1
    votos = int(input('VOTE [1]-Joao, [2]-Maria, [3]Jose: '))
    
    if votos == 1:
        qtd_votos_c1 += 1
        
    elif votos == 2:
        qtd_votos_c2 += 1 
        
    elif votos == 3:
        qtd_votos_c3 += 1 

print(f'Candidato 1 Joao teve {qtd_votos_c1} votos')
print(f'Candidato 2 Maria teve {qtd_votos_c2} votos')
print(f'Candidato 3 Jose teve {qtd_votos_c3} votos')

# '''
# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos.
# '''

qtd_turmas = int(input('Digite a quantidade de turmas: '))

total_alunos = 0

for x in range(qtd_turmas):
    
    x+=1
    alunos_por_turma = int(input(f'Quantos alunos na turma {x}: '))
        
    if alunos_por_turma > 40:
         print('As turmas não podem ter mais que 40 alunos: ')
            
    else:
        total_alunos += alunos_por_turma
        qtd_media = total_alunos / qtd_turmas

print(f'A quantidade media de alunos por turma é: {qtd_media}')

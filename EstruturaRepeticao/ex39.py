'''
Faça um programa que leia dez conjuntos de dois valores, 
o primeiro representando o número do aluno e o segundo 
representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas
'''

n_alunos = [1,2,3,4,5,6]

nome_alunos = ['alberto', 'thays', 'igor', 'jose', 'arnaldo', 'danilo' ]

altura_alunos = [170, 180, 190, 150, 200,250]

verificador_maior_altura = 0
verificador_menor_altura = 0

verificar_aluno_maior_altura = None
verificar_aluno_menor_altura = None


for i, nome in enumerate(n_alunos):
    altura_indv_aluno = altura_alunos[i]
    
    if altura_indv_aluno > verificador_maior_altura:
        verificador_maior_altura = altura_indv_aluno
        verificar_aluno_maior_altura = n_alunos[i]

    if altura_indv_aluno < verificador_menor_altura or verificador_menor_altura == 0:
        verificador_menor_altura = altura_indv_aluno
        verificar_aluno_menor_altura = n_alunos[i]

print(f'O aluno mais alto é o {nome_alunos[verificar_aluno_maior_altura - 1]} com {verificador_maior_altura} de altura')
print(f'O aluno mais baixo é o {nome_alunos[verificar_aluno_menor_altura - 1]} com {verificador_menor_altura} de altura')


    
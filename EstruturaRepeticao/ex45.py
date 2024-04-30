# '''
# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar 
# com o gabarito da prova e assim calcular o total de acertos e a nota (
# tribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema 
# deve ser feita uma pergunta se outro aluno vai utilizar o sistema.   
# Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;✅
# A Média das Notas da Turma.✅
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir isto você poderia incrementar o programa permitindo 
# que o professor digite o gabarito da prova antes dos alunos usarem o programa.
# '''
gabarito = []

qtd_questoes = int(input('Digite a quantidade de questões: '))

for q in range(qtd_questoes):
    q+=1
    resposta = input(f'Professor digite a resposta {q}ª: ')
    gabarito.append(resposta)

print('')

acertos_total = 0
erros_total = 0
n_aluno = 0

maior_acerto = 0
menor_acerto = float('inf')

aluno_maior_acerto = 0
aluno_menor_acerto = 0

print('--------------RESPOSTA ALUNOS--------------')
while True:

    acertos_por_aluno = 0
    erros_por_aluno = 0

    n_aluno +=1

    for i, gab in enumerate(gabarito):
        i+=1
        
        resposta = input(f'Digite a {i}ª resposta: ')

        if resposta in gab:
            acertos_por_aluno +=1
            acertos_total +=1
        else:
            erros_por_aluno +=1
            erros_total +=1

    if acertos_por_aluno > maior_acerto:
        maior_acerto = acertos_por_aluno
        aluno_maior_acerto = n_aluno

    if acertos_por_aluno < menor_acerto:
        menor_acerto = acertos_por_aluno
        aluno_menor_acerto = n_aluno

    continuar = input('Deseja continuar [S] ou [N]: ')
    print('')

    if continuar.upper() == 'N':
        print(f'Aluno {n_aluno}')
        print(f'Acertos: {acertos_por_aluno}')
        print(f'Erros: {erros_por_aluno}')
        
        print('')
        break

    else:
        print(f'Aluno {n_aluno}')
        print(f'Acertos: {acertos_por_aluno}')
        print(f'Erros: {erros_por_aluno}')
        print('')
        continue

    

print(f'acertos total: {acertos_total}')
print(f'erros total: {erros_total}')

print('')

media = acertos_total / n_aluno

print(f'A media de notas da turma é de {media}')

print('')

print(f'Total alunos usaram o sistema: {n_aluno}')

print(f'O aluno com mais acertos foi o {aluno_maior_acerto} com {maior_acerto} acertos')
print(f'O aluno com menos acertos foi o {aluno_menor_acerto} com {menor_acerto} acertos')



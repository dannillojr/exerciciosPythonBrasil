'''
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.

'''
media_alunos = []

contador = 0
qtd_alunos_acima_media = 0

while True:
    contador +=1
    somador_notas = 0

    if contador == 11:
        break
    else:
        print(' ')
        print(f'Nota aluno {contador}')
        
        for nota in range(1,5):
            notas = float(input(f'Digite a {nota}ª: '))
            somador_notas += notas
            media_aluno = somador_notas / 4
        
        media_alunos.append(media_aluno)

print(' ')            
for media in media_alunos:
    if media >= 7.0:
        qtd_alunos_acima_media +=1
print(f'{qtd_alunos_acima_media} alunos atingiram a meta ...')
    
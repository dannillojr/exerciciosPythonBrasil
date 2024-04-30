# '''
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# '''
numero = int(input('Montar tabuada de: '))

inicio = int(input('Començar por: '))
termino = int(input('terminar em: '))

print(f'')

if termino < inicio:
    print('Ai não né termino menor que o inicio ?')
else:
    print(f'Vou montar a tabuada de {numero} começando em {inicio} terminando em {termino}: ')
    for i in range(inicio, termino+1):

        resultado = i * numero
        print(f'{i} X {numero} = {resultado}')
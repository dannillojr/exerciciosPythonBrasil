# '''
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# '''
numero = int(input('Numero que deseja vê a tabuada: '))
print(f'A tabuada de {numero} é 👇')
for i in range(10):
    i += 1
    resultado = i * numero
    print(f'{i} X {numero} = {resultado}')
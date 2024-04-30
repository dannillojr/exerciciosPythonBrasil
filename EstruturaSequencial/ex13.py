'''
Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
h = input('Digite sua altura em metros: ')
sexo = input('Você é homem ou mulher [M] or [F]: ')

if sexo.lower() == 'm':
    peso_ideal = (72.7 * float(h)) - 58
    print(f'Seu peso ideal é : {peso_ideal:.2f}')

elif sexo.lower() == 'f':
    peso_ideal = (62.1 * float(h)) - 44.7
    print(f'Seu peso ideal é : {peso_ideal:.2f}')

else:
    print('Digite um dos sexos citados [M] para masculino, [F] para femenino')

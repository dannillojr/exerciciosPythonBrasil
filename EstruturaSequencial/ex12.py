'''
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''
altura = input('Digite dua altura em m: ')

peso_ideal = (72.7*float(altura)) - 58

print(f'Peso ideal é: {peso_ideal}')
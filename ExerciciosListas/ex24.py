# '''
# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
# simulando os lançamentos dos dados.
# '''
import random

def gera_numeros_aleatorios():
    valor = random.randint(1,6)
    return valor

valores = []
contadores = [0] * 6

for _ in range(1,100+1):
    valor = gera_numeros_aleatorios()
    valores.append(valor)

for v in valores:
    if v == 1:
        contadores[0] +=1
    elif v == 2:
        contadores[1] +=1
    elif v == 3:
        contadores[2] +=1
    elif v == 4:
        contadores[3] +=1
    elif v == 5:
        contadores[4] +=1
    elif v == 6:
        contadores[5] +=1

for i, cont in enumerate(contadores):
    i+=1
    print(f'O numero {i} apareceu {cont} vezes')
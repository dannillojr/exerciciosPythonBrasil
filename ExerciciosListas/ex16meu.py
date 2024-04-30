'''
Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões.

O vendedor recebe $200 por semana mais 9% de suas vendas brutas daquela semana. 

Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9% de $3000, 
ou seja, um total de $470.

Escreva um programa (usando um array de contadores) que determine quantos 
vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''
import os
contadores = [0] * 9 

salarios = []

for i in range(9):
    vendas_brutas = float(input("Informe o valor das vendas brutas do vendedor: $"))
    bonus = 200
    bonificacao = (9/100) * vendas_brutas
    salario_final = bonus + vendas_brutas + bonificacao 
    salarios.append(salario_final)
    print(salario_final)

print(salarios)

for salario in salarios:
    
    if salario >= 200 and salario <= 299:
        contadores[0] += 1  
    elif salario >= 200 and salario <= 399:
        contadores[1] += 1
    elif salario >= 400 and salario <= 499:
        contadores[2] += 1
    elif salario >= 500 and salario <= 599:
        contadores[3] += 1
    elif salario >= 600 and salario <= 699:
        contadores[4] += 1
    elif salario >= 700 and salario <= 799:
        contadores[5] += 1
    elif salario >= 800 and salario <= 899:
        contadores[6] += 1
    elif salario >=900 and salario <= 999 :
        contadores[7] += 1
    else:
        contadores[8] += 1

os.system('cls')

for i, contador in enumerate(contadores[:-1]):
    print(f"${200 + i * 100} - ${299 + i * 100}: {contador}")

print(f"${1000} em diante: {contadores[-1]}")

# print('$200 - $299',contadores_1)
# print("$300 - $399",contadores_2)
# print("$400 - $499",contadores_3)
# print("$500 - $599",contadores_4)
# print("$600 - $699",contadores_5)
# print("$700 - $799",contadores_6)
# print("$800 - $899",contadores_7)
# print("$900 - $999",contadores_8)
# print('$1000 em diante',contadores_9)

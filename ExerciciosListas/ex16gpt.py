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
contadores = [0] * 9  # Usando uma lista para contadores

salarios = []

# Loop para calcular os salários dos vendedores
for _ in range(8):
    # Validação de entrada para garantir que o valor seja um número válido
    while True:
        try:
            vendas_brutas = float(input("Informe o valor das vendas brutas do vendedor: $"))
            if vendas_brutas >= 0:
                break
            else:
                print("Por favor, informe um valor válido.")
        except ValueError:
            print("Por favor, informe um valor numérico válido.")

    bonus = 200
    bonificacao = (9 / 100) * vendas_brutas
    salario_final = bonus + vendas_brutas + bonificacao 
    salarios.append(salario_final)
    
print('')
# Contagem dos salários em cada faixa
print('Salario finais')
for salario in salarios:
    print(f'{salario}', end=' -- ')
    if salario < 1000:
        indice = int((salario - 200) // 100)
        contadores[indice] += 1
    else:
        contadores[-1] += 1
print('')
print('')
# Impressão dos resultados
for i, contador in enumerate(contadores[:-1]):
    print(f"${200 + i * 100} - ${299 + i * 100}: {contador}")

print(f"${1000} em diante: {contadores[-1]}")






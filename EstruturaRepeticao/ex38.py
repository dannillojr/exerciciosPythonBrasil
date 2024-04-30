
# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem 
# ao dobro do percentual do ano anterior. Faça um programa que determine o 
# salário atual desse funcionário. Após concluir isto, altere o programa permitindo 
# que o usuário digite o salário inicial do funcionário.

salario_inicial = float(input('Digite o salario: '))
ano_contratacao = int(input('Digite ano de contratação: '))
aumento = float(input('Digite o aumento: '))

aumento = aumento / 100

ano_aumento = ano_contratacao + 1

novo_salario = salario_inicial + (aumento * salario_inicial)

print(f'Ano: {ano_aumento} salario: R${novo_salario}, {aumento:.2%}')

while ano_aumento <= 2024:

    ano_aumento += 1
    aumento = aumento * 2

    novo_salario = salario_inicial + (aumento * salario_inicial)
    print(f'Ano: {ano_aumento} salario: R${novo_salario}, {aumento:.2%}')

    

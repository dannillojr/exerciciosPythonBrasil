'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

'''
salario = float(input('SALARIO: '))

#salario menor que 280
if salario < 280:
    aumento_porcetagem = 20/100
    valor_aumento = aumento_porcetagem * salario
    salario_reajustado = salario + (aumento_porcetagem * salario)

    print(f'Salario antes do reajuste: R${salario}')
    print(f'o percentual de aumento aplicado: {aumento_porcetagem:.1%}')
    print(f'o valor do aumento: R${valor_aumento}')
    print(f'o novo salário, após o aumento R${salario_reajustado}')

#salario entre 280 e 700
elif salario >= 280 and salario <= 700:

    aumento_porcetagem = 15/100
    valor_aumento = aumento_porcetagem * salario
    salario_reajustado = salario + (aumento_porcetagem * salario)

    print(f'Salario antes do reajuste: R${salario}')
    print(f'o percentual de aumento aplicado: {aumento_porcetagem:.1%}')
    print(f'o valor do aumento: R${valor_aumento}')
    print(f'o novo salário, após o aumento R${salario_reajustado}')

#Salario mario que 1500
elif salario >= 1500:

    aumento_porcetagem = 5/100
    valor_aumento = aumento_porcetagem * salario
    salario_reajustado = salario + (aumento_porcetagem * salario)

    print(f'Salario antes do reajuste: R${salario}')
    print(f'o percentual de aumento aplicado: {aumento_porcetagem:.1%}')
    print(f'o valor do aumento: R${valor_aumento}')
    print(f'o novo salário, após o aumento R${salario_reajustado}')
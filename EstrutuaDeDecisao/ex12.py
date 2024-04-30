'''
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do 
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Imposto de Renda
3% para o Sindicato

o FGTS corresponde a 11% do Salário Bruto (não desconta do bruto empresa que deposita)

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00

        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

'''
valor_hora = float(input('Digite valor da hora trabalhada: '))
horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
print('')

ir = 5/100
inss = 10/100
fgts = 11/100

salario_bruto = horas_trabalhadas * valor_hora

desconto_ir = ir * salario_bruto
desconto_inss = inss * salario_bruto
valor_fgts = fgts * salario_bruto

total_desconto = desconto_inss + desconto_ir
salario_liquido = salario_bruto - total_desconto

if salario_bruto <= 900:
    ir = 0
    total_desconto = desconto_inss
    salario_liquido = salario_bruto - desconto_inss
    print(f'Salario bruto: ({valor_hora} * {horas_trabalhadas}):         R${salario_bruto}')
    print(f'(-) IR {ir:.1%}:                         R${ir}')
    print(f'(-) INSS ({inss:.1%}):                      R${desconto_inss}')
    print(f'FGTS ({fgts:.1%}):                          R${valor_fgts}')

    print('')

    print(f'Total de descontos:                  R${total_desconto}')
    print(f'Salario liquido:                     R${salario_liquido}')

elif salario_bruto > 900 and salario_bruto <= 1500:
    salario_liquido = salario_bruto - total_desconto
    print(f'Salario bruto: ({valor_hora} * {horas_trabalhadas}):         R${salario_bruto}')
    print(f'(-) IR ({ir:.1%}):                         R${desconto_ir}')
    print(f'(-) INSS ({inss:.1%}):                      R${desconto_inss}')
    print(f'FGTS ({fgts:.1%}):                          R${valor_fgts}')

    print('')

    print(f'Total de descontos:                  R${total_desconto}')
    print(f'Salario liquido:                     R${salario_liquido}')

elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 10/100
    desconto_ir = ir * salario_bruto
    salario_liquido = salario_bruto - desconto_ir - desconto_inss
    total_desconto = desconto_inss + desconto_ir

    print(f'Salario bruto: ({valor_hora} * {horas_trabalhadas}):         R${salario_bruto}')
    print(f'(-) IR ({ir:.1%}):                         R${desconto_ir}')
    print(f'(-) INSS ({inss:.1%}):                      R${desconto_inss}')
    print(f'FGTS ({fgts:.1%}):                          R${valor_fgts}')

    print('')

    print(f'Total de descontos:                  R${total_desconto}')
    print(f'Salario liquido:                     R${salario_liquido}')

elif salario_bruto > 2500 :
    ir = 20/100
    desconto_ir = ir * salario_bruto
    salario_liquido = salario_bruto - desconto_ir - desconto_inss
    total_desconto = desconto_inss + desconto_ir
    print(f'Salario bruto: ({valor_hora} * {horas_trabalhadas}):         R${salario_bruto}')
    print(f'(-) IR ({ir:.1%}):                         R${desconto_ir}')
    print(f'(-) INSS ({inss:.1%}):                      R${desconto_inss}')
    print(f'FGTS ({fgts:.1%}):                          R${valor_fgts}')

    print('')

    print(f'Total de descontos:                  R${total_desconto}')
    print(f'Salario liquido:                     R${salario_liquido}')


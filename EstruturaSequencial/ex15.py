'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

valor_hora = input('Digite o valor da sua hora de trabalho: ')
qtd_horas_mes = input('Quantas horas trabalhou esse mês: ')

salario_bruto = float(valor_hora) * float(qtd_horas_mes)

imposto_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicado = salario_bruto * (5/100)

salario_liquido = salario_bruto - imposto_renda - inss - sindicado

print(f'Salario BRUTO: R${salario_bruto}')
print(f'Desconto Imposto de renda: R${imposto_renda}')
print(f'Desconto INSS: R${inss}')
print(f'Desconto Sindicado: R${sindicado}')
print(f'Seu salario liquido é : R${salario_liquido}')
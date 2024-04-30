'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: 

até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

'''
qtd_litros = float(input('Digite a quantidade de litros: '))
combustivel = input('Qual combustivel usou A - (álcool) G - (gasolina): ')

alcool_litro = 1.90
gasolina_litro = 2.50

valor_total_alcool = qtd_litros * alcool_litro
valor_total_gasolina = qtd_litros * gasolina_litro


if combustivel.upper() == 'A':

    if qtd_litros > 20:
        desconto = 5/100
        valor_total_alcool -= (desconto * valor_total_alcool)
        print(f'R${valor_total_alcool:.2f}')

    elif qtd_litros <= 20:
        desconto = 3/100
        valor_total_alcool = valor_total_alcool - (desconto * valor_total_alcool)
        print(f"R${valor_total_alcool:.2f}") 

elif combustivel.upper() == 'A':

    if qtd_litros <= 20:
        desconto = 4/100
        valor_total_gasolina -= (desconto * valor_total_gasolina)
        print(f'R${valor_total_gasolina:.2f}')

    elif qtd_litros > 20:
        desconto = 6/100
        valor_total_gasolina -= (desconto * valor_total_gasolina)
        print(f'R${valor_total_gasolina:.2f}')

else:
    print('Por favor, digite "A" para álcool ou "G" para gasolina.')

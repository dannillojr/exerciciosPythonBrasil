'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
valor do desconto e valor a pagar.

'''
def gera_nota(*args):
    carne, kg_carne, valor_kg, uso_cartao, desconto, preco_total, forma_pagamento = args
    return (
        f'PRODUTO: {carne}\n'
        f'QUILO PRODUTO: {kg_carne}kg\n'
        f'VALOR DO KG: R${valor_kg:.2f}/kg\n'
        f'USO CARTÃO: {uso_cartao}\n'
        f'DESCONTO: {desconto}%\n'
        f'VALOR A SER PAGO: R${preco_total:.2f}\n'
        f'FORMA DE PAGAMENTO: {forma_pagamento}\n'
    ) 

carne = input('Digite a carne comprada: ')
kg_carne = float(input('Digite o kg da carne comprada: '))
uso_cartao = input('Vai usar cartão (sim/não): ').lower()

if uso_cartao == 'sim':
    forma_pagamento = 'cartão'
else:
    forma_pagamento = 'dinheiro'

print('')

# Definindo o desconto como 0 inicialmente
desconto = 0

if carne.lower() == 'file duplo':
    if kg_carne <= 5:
        preço = 4.90
    elif kg_carne > 5:
        preço = 5.80

    # Aplicando desconto se o cliente optar por usar o cartão
    if uso_cartao == 'sim':
        desconto = 5
        valor_pagar_file = preço * kg_carne
        valor_pagar_file -= desconto / 100 * valor_pagar_file
    else:
        valor_pagar_file = preço * kg_carne
    
    print(gera_nota(carne, kg_carne, preço, uso_cartao, desconto, valor_pagar_file, forma_pagamento))

elif carne.lower() == 'alcatra':
    if kg_carne <= 5:
        preço = 5.90
    elif kg_carne > 5:
        preço = 6.80

    # Aplicando desconto se o cliente optar por usar o cartão
    if uso_cartao == 'sim':
        desconto = 5
        valor_pagar_alcatra = preço * kg_carne
        valor_pagar_alcatra -= desconto / 100 * valor_pagar_alcatra
    else:
        valor_pagar_alcatra = preço * kg_carne
    
    print(gera_nota(carne, kg_carne, preço, uso_cartao, desconto, valor_pagar_alcatra, forma_pagamento))

elif carne.lower() == 'picanha':
    if kg_carne <= 5:
        preço = 6.90
    elif kg_carne > 5:
        preço = 7.80

    # Aplicando desconto se o cliente optar por usar o cartão
    if uso_cartao == 'sim':
        desconto = 5
        valor_pagar_picanha = preço * kg_carne
        valor_pagar_picanha -= desconto / 100 * valor_pagar_picanha
    else:
        valor_pagar_picanha = preço * kg_carne
    
    print(gera_nota(carne, kg_carne, preço, uso_cartao, desconto, valor_pagar_picanha, forma_pagamento))

else:
    print('Tipo de carne não reconhecido. Por favor, escolha entre "file duplo", "alcatra" ou "picanha".')

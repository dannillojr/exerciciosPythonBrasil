'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para 
a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro 
valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total 
de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, 
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''
import os

def Calcula_valor_pagamento(valor_prestacao, dias_atraso):
    multa = 3/100
    multa_dia = 1/100

    if dias_atraso == 0:
        return valor_prestacao
    else:
        valor_com_multa = valor_prestacao + (valor_prestacao * multa)
        valor_prestacao_com_atraso = valor_com_multa + (multa_dia * valor_prestacao * dias_atraso)
        return valor_prestacao_com_atraso

pagamentos = []

while True: 
    valo_prestacao = float(input('Digite o valor da prestação: '))

    if valo_prestacao == 0:
        os.system('cls')
        break
    else:

        dias_atraso = int(input('Digite a quantidade de dias atrasados: '))
        valor_a_pagar = Calcula_valor_pagamento(valo_prestacao, dias_atraso)

        pagamentos.append(valor_a_pagar)
        print(valor_a_pagar)

valor_total_pago = sum(pagamentos)
qtd_pagamentos = len(pagamentos)

print(f'{"----Relatorio----":^70}')
print(f'Você pagou {qtd_pagamentos} faturas, gastou um total de R${valor_total_pago:.2f} reais com os pagamentos')
print('')


    
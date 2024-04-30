# '''
# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1                                   0%
# 3                                  10%
# 6                                  15%
# 9                                  20%
# 12                                 25%

# Exemplo de saída do programa:
# Valor da Dívida  / Valor dos Juros/ Quantidade de Parcelas  /Valor da Parcela
# R$ 1.000,00        0                 1                       R$  1.000,00
# R$ 1.100,00       100                3                       R$    366,00
# R$ 1.150,00       150                6                       R$    191,67

# '''

valor = float(input('Digite o valor da divida: '))
print(' ')

parcelas = {
    1: 0,
    3: 0.10,
    6: 0.15,
    9: 0.20,
    12: 0.25

}

print(f'{"VARLOR DÍVIDA":<20} {"VALOR DOS JUROS":<20} {"QUANTIDADE DE PARCELAS":<20}   {"VALOR PARCELAS":<20}')
for numero_parcelas, juros in parcelas.items():
        
        valor_juros = valor * juros
        valor_divida = valor + valor_juros
        valor_parcela = valor_divida / numero_parcelas
        
        print(f'R${valor_divida:<20.2f} R${valor_juros:<20.2f} {numero_parcelas:<23.2f} R${valor_parcela:<20.2f}')



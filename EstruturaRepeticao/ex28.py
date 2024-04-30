# '''
# Faça um programa que calcule o valor total investido por um colecionador 
# em sua coleção de CDs e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.
# '''
qtd_cd = int(input('Quantos cd"s: '))

valor_total = 0

for x in range(qtd_cd):
    x+=1

    valor_unid_cd = float(input(f'Qual valor do {x}ª cd: '))
    valor_total += valor_unid_cd

    media  = valor_total/qtd_cd

print(f'O valor medio gasto nos CD"s foi de R${media:.2f}... por cd')
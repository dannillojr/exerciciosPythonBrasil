'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area_pintada / 6

latas_necessarias = int(litros_necessarios / 18)
galao_necessarios = int(litros_necessarios / 3.6)

if litros_necessarios % 18 != 0:
    latas_necessarias += 1
if litros_necessarios % 3.6 != 0:
    galao_necessarios += 1

preco_por_lata = 80.00
preco_por_galao = 25.00

preco_total_lata = latas_necessarias * preco_por_lata
preco_total_galao = galao_necessarios * preco_por_galao

qtd_lata_misturada = litros_necessarios // 18
resto_mistura = litros_necessarios % 18
qtd_galao_misturado = resto_mistura / 3.6

if resto_mistura % 3.6 != 0:
    qtd_galao_misturado += 1

preco_total_mistura = qtd_lata_misturada * preco_por_lata + qtd_galao_misturado * preco_por_galao

print(f"Quantidade de tinta necessária: {litros_necessarios:.2f} litros")
print(f"Preço para comprar apenas latas de 18 litros: R$ {preco_total_lata:.2f}")
print(f"Preço para comprar apenas galões de 3,6 litros: R$ {preco_total_galao:.2f}")
print(f"Preço para misturar latas e galões: R$ {preco_total_mistura:.2f}")




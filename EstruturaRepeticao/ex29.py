# 
# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que 
# contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a 
# atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na 
# tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, 
# que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50
# 
qtd_intens_cliente = input('Quantos itens o cliente vai comprar :')

preco_uni = 1.99

if qtd_intens_cliente.isdigit():
    qtd_intens_cliente = int(qtd_intens_cliente)
    
    for x in range(50):
        x+=1
        
        if qtd_intens_cliente < 0 or qtd_intens_cliente > 50:
            print('Limite de itens é de 50 por verificação... e obvio não pode ser um valor negativo..')
            break

        elif qtd_intens_cliente == x:
            print(f'Quantidade = {x} valor = {x * preco_uni}')
else:
    print('Digite apenas numeros')

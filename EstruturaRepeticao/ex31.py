# 
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e 
# agora possui uma loja de conveniências. 

# Faça um programa que implemente uma 
# caixa registradora rudimentar. 

# O programa deverá receber um número desconhecido 
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado 
# pelo operador para indicar o final da compra. O programa deve então mostrar o total 
# da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular 
# e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
# para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# 
#inicia o programa
while True:
    print('------LOJAS TABAJARA------')
    cont = 0
    valor_total = 0

    #loop para receber os produtos 
    while True:
        cont+=1
        valor_produtos = float(input(f'PRODUTO {cont}: '))

        if valor_produtos == 0:
            print('FINALIZADO')
            print(f'VALOR TOTAL R${valor_total}')
            break #finaliza com a entrada sendo 0 para calular o o total

        valor_total += valor_produtos #soma os produtos referente ao total a pagar


    pagamento = float(input('VALOR RECEBIDO: ')) #recebe o pagamento

    while pagamento < valor_total: #loop se o pagamento for menor que o valor total não tem como calcular o troco
        
        print('Não pode receber menos que o valor total anta...')
        pagamento = float(input('VALOR RECEBIDO: '))

    troco = pagamento - valor_total #calcula o troco

    print(f'Troco = {troco}')

    continuar = input('Deseja continuar [S] - [N]: ') # verificar se vai continuar o loop
            
    if continuar.upper() == 'S': # se sim inicia tudo de novo
        continue
    else: # se não finaliza e pronto
        print('Encerrado')
        break





        




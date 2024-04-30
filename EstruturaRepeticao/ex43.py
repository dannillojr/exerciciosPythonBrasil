# '''
# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço

# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.
# '''

#dicionario com os produtos e o preços
produtos = {
    100: {'item':'Cachorro quente', 'valor': 1.20},
    101: {'item':'Bauru Simples', 'valor': 1.30},
    102: {'item':'Bauru com ovo', 'valor': 1.50},
    103: {'item':'Hambúrguer', 'valor': 1.20},
    104: {'item':'Cheeseburguer', 'valor': 1.30},
    105: {'item':'Refrigerante', 'valor': 1.00},

}

#lista vazia que vai recer um dicionario equivalente ao produtos que o cliente vai comprar
pedido = []

#variavel que vai começar com zero e ir somando os valores das compras
valor_total = 0

print(f'{"CODIGO":<20} {"PRODUTO":<20} {"PRECO":<20}')

#i iteração sobre o dicionario para exibir os valores como um cartaz
for cod, valor in produtos.items():
    
    print(f'{cod:<20} {valor['item']:<20} R${valor['valor']:.2f}')

print('')

# laco loop de solicitação de pedidos e quantidades
while True:
    cod_produto = int(input('CODIGO DO PRODUTO ([-1] para parar): '))
    
    #verifica se o cod de protudo digitado é igua a -1 para parar o programa
    if cod_produto == -1:
        break
    
    #Verifica de o cod digitado esta dento da lista de produtos
    if cod_produto in produtos:
        quantidade  = int(input('QUANTIDADE DESEJADA: '))#se o codigo de produto tiver na lista pede a quantidade
        print('')
        #entra no dicionario "produtodo" o primeiro [] acessa o codigo o segundo [] acessa o valor do preço e armazena na variavel
        preco_por_item = produtos[cod_produto]['valor'] 

        #pega o preço da variavel "preco_item" multiplica pela quantidade para calcular o valor a ser pago
        valor_total_item = preco_por_item * quantidade 

        #calcula o valor total inicialemte iniciada com 0 e q cada laço vai simento com o valor da variavel "total_intem"
        valor_total += valor_total_item

        #vai adicionando os pedidos do cliente em uma lista de dicionarios inicilmente começou vazio e a cada iteração foi sendo adicionado mais uma compra
        pedido.append({
                        'item': produtos[cod_produto]['item'],
                        'quantidade': quantidade ,
                        'preco/item': preco_por_item,
                        'total': valor_total_item
                        })
    else:
        print('CODICO INVALIDO')

print('')

print(f'{"PRODUTO":<20} {"QUANTIDADE":<20} {"PRECO/ITEIM":<20} {"TOTAL/ITEM":<20}')

# itera sobre a lista de pedido que foi iniciada fazia o foi sendo adicionado chaves e valores no laço
for item_pedido in pedido:
    print(f"{item_pedido['item']:<20} {item_pedido['quantidade']:<20} {item_pedido['preco/item']:<20.2f} {item_pedido['total']:<20.2f}")

print(' ')

print(f'TOTAL DO PEDIDO: R${valor_total:.2f}')



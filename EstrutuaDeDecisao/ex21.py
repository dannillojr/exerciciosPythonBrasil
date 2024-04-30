'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas
notas de cada valor serão fornecidas. 

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 

O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais,
 o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais,
 o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

'''

#solicita valor a ser sacado
saque = float(input('Digite o valor a ser sacado: '))

#lista de notas disponiveis
notas_disponiveis = [100, 50, 10, 5, 1]

#dicionario vazio que vai receber as notas e as quantidades de notas a serem sacadas priorizando as de maior valor
notas_fornecidas = {}


# verificar se o valor a ser sacado está entre o min e max permitido...
if saque < 10 or saque > 600:
    print('valor invalido gentileza quantidade minimo de saque é R$10 e max de R$ 600...')
else:
    #itera sobre cada nota diponivel dentro da lista de notas disponiveis
    for notas in notas_disponiveis:

        #calcula quantas notas são necessarias para da o valor a ser sacado
        qtd_notas = saque // notas

        #subtrai o valor total de saque pelas quantidades de notas para diminuir o valor e não repetir os calculos
        saque -= qtd_notas * notas
        
        #adiciona chave notas: para o valor qtd_notas ao dicionario exibindo assim a quantidade de notas necessarias para 
        #O o valor a ser sacado
        notas_fornecidas[notas] = qtd_notas
    
    #itera sobre o dicionario pegando as chaves e valores trasnformando em tupla com função items()
    for notas, quantidade in notas_fornecidas.items():

        #veirifica se o valor quantidade está mior que zero se sim exibe a chave e o valor informando a quantidade de notas
        #e o valor equivalente ao valor a ser sacado
        if quantidade > 0:
            print(f'{int(quantidade)} Notas de R${notas:.2f}')


'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças 

adquiridas e escreva o valor a ser pago pelo cliente.

'''


try:
    kg_morango = float(input('Quantidade de KG do morango: '))
    kg_maca = float(input('Quantidade de KG da maçã: '))

    kg_total_frutas = kg_morango + kg_maca

    valor_pagar_morango = 0
    valor_pagar_maca = 0
    #verificação jg morango
    if kg_morango <= 5:
        valor_kg_morango = 2.50
        valor_pagar_morango = kg_morango * valor_kg_morango

            
    elif kg_morango > 5:
        valor_kg_morango = 2.20
        valor_pagar_morango = kg_morango * valor_kg_morango


    #verificação kg maça
    if kg_maca <= 5:
        valor_kg_maca = 1.80
        valor_pagar_maca = kg_maca * valor_kg_maca

    elif kg_maca > 5:
        valor_kg_maca = 1.50 
        valor_pagar_maca = kg_maca * valor_kg_maca

    total_pagar = valor_pagar_morango + valor_pagar_maca

    print('')

    print(f'Valor morango individual = R${valor_pagar_morango}')
    print(f'Valor maça individual = R${valor_pagar_maca}')

    print('')

    print(f'Quantidade de KG total: {kg_total_frutas}kg')

    print('')

    print(f'Valor total a ser pago sem desconto R${total_pagar:.2f}')

    print('')

    if kg_total_frutas > 8 or total_pagar > 25:
        desconto = 10/100
        total_pagar_desconto = total_pagar - (desconto * total_pagar)
        print(f'Você tem direito a {desconto:.1%} de desconto pois a soma dos quilos das frutas é  maior que 8kg')
        print('ou a soma das duas frutas passam de R$25 reais ')

        print('')

        print(f'Valor a ser pago com desconto R${total_pagar_desconto}')


except:
    print('')
    print('Certifique que está preenchendo os campos corretamente')
    print('Somentes valores positivos')
    print('Não digite letras etc, apenas numeros..')
    




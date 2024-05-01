'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários 
cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, 
descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. 
Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada 
colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
'''
import os
salarios = []
abonos = []

abono = 0
reajuste = 20/100
piso = 100

try:
    while True:
        try:
            salario = float(input('Digite o salario: '))

            if salario == 0:
                os.system('cls')
                break
            else:
                salarios.append(salario)
        except:
            print('Digite uma entrada valida')
        
    for salario in salarios:

        if salario >= 1000:
            abono = reajuste * salario
            abonos.append(abono)
            
        elif salario < 1000:
            abono = piso
            abonos.append(abono)

    qtd_colaboradores = len(salarios)
    total_gastos_abono = sum(abonos)    
    maior_pagamento_abono = max(abonos)

    print('')       

    print('PROJEÇÃO DE GASTOS COM ABONO')
    print('============================')
    print('')

    for s in salarios:
        print(f'Salario: {s:.2f}')

    print('')

    print(f'{"SALARIOS":<23} {"ABONOS":<10}')
    for s, a in zip(salarios, abonos):
        print(f'R${s:<20.2f} R${a:<10.2f}')

    print('')

    print(f'Foram processados {qtd_colaboradores} Colaboradores')
    print(f'Total gasto com abonos: R${total_gastos_abono:.2f}')
    print(f'O maior valor de abono pago: R${maior_pagamento_abono:.2f}')
except:
    print('Encerrado sem nenhuma entrada valida')
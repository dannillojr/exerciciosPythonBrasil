'''
Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato 
D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida
'''
def data_por_extenso(data):
    dia, mes, ano = map(int, data.split('/'))
    meses = ['jan','fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'  ]

    mes_extenso = meses[mes - 1]

    data_formatada = f'Dia {dia} de {mes_extenso} de {ano}'

    return data_formatada

data = data_por_extenso("04/05/2024")

print(data)









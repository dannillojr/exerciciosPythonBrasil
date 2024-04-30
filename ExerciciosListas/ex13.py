'''
Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Após isto, 

calcule a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram 

(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

temperaturas_med = []

soma_med = 0

meses = {
    1: {'Mes': 'jan'},
    2: {'Mes': 'fev'}, 
    3: {'Mes': 'mar'},
    4: {'Mes': 'abr'},
    5: {'Mes': 'mai'},
    6: {'Mes': 'jun'},
    7: {'Mes': 'jul'},
    8: {'Mes': 'ago'},
    9: {'Mes': 'set'},
    10: {'Mes': 'out'},
    11: {'Mes': 'nov'},
    12: {'Mes': 'dez'},

}

for m in range(1, 13):
    temp_mes = float(input(f'Digite a temperatura media do mês {m}: '))
    temperaturas_med.append(temp_mes)

for m_mes in temperaturas_med:
    soma_med += m_mes

media_ano = soma_med / 12

print('')
print(f'A media anual de temperaturas foi: {media_ano}')
print('O meses que tivera temperatura maio que a media foram: 👇')
print('')
for i, temp in enumerate(temperaturas_med):
    i+=1
        
    if temp > media_ano:
        print(f'{i} - {meses[i]['Mes']} temperatura - {temp}')

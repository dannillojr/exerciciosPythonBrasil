# '''
# Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. 
# Para finalizar o conjunto de votos tem-se o valor zero.
# '''

candidatos = {
    1:'Lula' ,
    2:'João',
    3:'Marcos',
    4:'Bolsonaro',
    5:'Branco',
    6:'Nulo',
}
contador_lula = 0
contador_joao = 0
contador_marcos = 0
contador_bolso = 0
contador_branco = 0
contador_nulo = 0


print(f'{"CANDIDATO":<20} {"COD/VOTO"}')
for chave, condidato in candidatos.items():
    print(f'{condidato:<20} {chave:<20}')

print(' ')
while True:
    voto = int(input('Digite o COD do seu candidato ([0] para finalizar): '))

    if voto == 0:
        break

    if voto == 1:
        contador_lula += 1

    elif voto == 2:
        contador_joao +=1
    
    elif voto == 3:
        contador_marcos +=1

    elif voto == 4:
        contador_bolso +=1

    elif voto == 5:
        contador_branco +=1

    elif voto == 6:
        contador_nulo +=1

    else:
        print('Voto invalido..')
    

total_votos = contador_lula + contador_joao + contador_marcos + contador_bolso + contador_branco + contador_nulo
porcetam_votos_nulos = (contador_nulo / total_votos) * 100
porcetam_votos_brancos = (contador_branco / total_votos) * 100


resultados =[
    contador_lula,
    contador_joao,
    contador_marcos,
    contador_bolso,
    contador_branco,
    contador_nulo,
]
print(' ')
print(f'{"CANDIDATO":<20} {"COD/VOTO":<20} {"QTD VOTOS":<20}')

for chave, condidato in candidatos.items():
    votos = resultados[chave-1]
    print(f'{condidato:<20} {chave:<20} {votos:<20}')

print(' ')
print(f'TOTAL VOTOS GERAL: {total_votos} ')
print('')
print(F'A percentagem de votos NULOS sobre o total de votos: {porcetam_votos_nulos:.2f}%')
print(F'A percentagem de votos BRANCOS sobre o total de votos: {porcetam_votos_brancos:.2f}%')
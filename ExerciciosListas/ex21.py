'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 

Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima 
possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
'''
import os

carros = []
km_litro = []
l_gasolina = 2.50
distancia_a_percorrer = 1000
valor_maior_km_litro = 0
carro_maior_km_litro = ''


while True: 
    try:
        nome_carro = input('Digite o nome/modelo do carro [0] para encerrar: ')
        
        if nome_carro == '0':
            os.system('cls')
            break
        else:
            
            litros_km = float(input('QUANTOS KM POR LITRO: '))
            carros.append(nome_carro)
            km_litro.append(litros_km)
    except:
        print('ALGUM VALOR INVALIDO em nome digite apenas letras, em km por litro apenas numeros')


print(' ')
print(f'{"-"*30}RETALTORIO FINAL{"-"*30}')
print(' ')

print(f'{"VEICULO":<17} {"KM/LITRO":<20} {"QTD_LITROS/1000KM":<25} {"VALOR/1000KM":<14}')
print('')
for carro, km_l in zip(carros, km_litro):
    qtd_litro_1000km = 1000 / km_l
    valor_litro = qtd_litro_1000km * l_gasolina

    if km_l > valor_maior_km_litro:
        valor_maior_km_litro = km_l
        carro_maior_km_litro = carro

    print(f'{carro:<14} {km_l:>8.2f} km {qtd_litro_1000km:>21.1f}L {"R$":>20}{valor_litro:.2f}')

print('')

print(f'O veiculo que consome menos é o {carro_maior_km_litro}')

print('Nenhuam entrada encerrando ...')
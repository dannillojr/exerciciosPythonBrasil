'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe
 ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, 
 que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa 
 (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
 Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos 
 concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
'''
import os
nome_sistemas = ['Windows Server','unix','Linux','Netware','Mac os','outros',]
numero_sistemas = [1,2,3,4,5,6]
contadores = [0] * 6
porcetagens = []

print(f'{"COD/VOTO":<18} {"SISTEMAS":<15}')

for nome, numero in zip(nome_sistemas, numero_sistemas):
    print(f'{numero:<18} {nome:<15}')

print('')

while True:
    try:
        voto = int(input('VOTE [-1] para encerrar: '))
        
        if voto == -1:
            os.system('cls')
            break
        else:
            if voto == 1:
                contadores[0] += 1
            elif voto == 2:
                contadores[1] += 1
            elif voto == 3:
                contadores[2] += 1
            elif voto == 4:
                contadores[3] += 1
            elif voto == 5:
                contadores[4] += 1
            elif voto == 6:
                contadores[5] += 1
            elif voto == 7:
                contadores[6] += 1
            elif voto not in numero_sistemas:
                print('VOTO INVALIDO')

    except:
        print('VOTO INVALIDO, Informe um valor valido.')
try:
    total_votos = sum(contadores)

    print('')
    print(f'{"SISTEMAS":<18} {"TOTAL/VOTOS":<15} {"PORCETAGEM/TOTAL/VOTOS":<15}')
    print('')

    for sistema, qtd_votos in zip(nome_sistemas, contadores):
        porcetagem = (qtd_votos/total_votos) * 100
        porcetagens.append(porcetagem)
        print(f'{sistema:<20} {qtd_votos:<20} {porcetagem:.2f}%')

    print('')

    maior_porcetagem = max(contadores) / total_votos * 100
    sistema_mais_votado = []

    for i in range(len(nome_sistemas)):
        if contadores[i] == max(contadores):
            sistema_mais_votado.append(nome_sistemas[i])
        
    if len(sistema_mais_votado) == 1:
        resultado = f'O sistema mais votado foi {sistema_mais_votado[0]} com {maior_porcetagem:.2f}% dos votos'
    else:
        resultado = f'{", ".join(sistema_mais_votado)} empataram deve ser realizado uma segunda chamada'

    print('')
    print(f'Foi computado {total_votos} votos')
    print('')
    print(resultado)
except:
    print('ENCERRADO')
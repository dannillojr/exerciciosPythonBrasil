'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random

def jogar_crabs():
    print('Bem vindo ao jogo CRABS')
    print('')

    while True:
        input('APERTE ENTER PARA LANÇAR OS DADOS ')
        print('')
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)

        resultado = dado_1 + dado_2

        print(f'VOCE LANÇOU OS DADOS RESULTADO FOI:  {resultado}')
        print('')

        if resultado == 7 or resultado == 11:
            print(f'Você tirou {resultado} = NATURAL -> VENCEU 🥳')
            break

        elif resultado == 2 or resultado == 3 or resultado == 12:
            print(f'Você tirou {resultado} = "CRAPS" -> PERDEU 🙁')

        else:
            print(f'Seu ponto é {resultado}')
            print('')
            while True:
                input('APERTE ENTER PARA LANÇAR OS DADOS NOVAMENTE ')
                print('')
                dado_1 = random.randint(1, 6)
                dado_2 = random.randint(1, 6)
                resultado_2 = dado_1 + dado_2
                print(f'LANÇOU O DADO NOVAMENTE O TOTAL É {resultado_2}')
                print('')

                if resultado_2 == resultado:
                    print('VOCE TIROU SEU PONTO - VENCEU 🥳')
                    return
                elif resultado_2 == 7:
                    print(f'VOCE TIROU {resultado_2} -> perdeu 🙁')
                    return

while True:
    jogar_crabs()
    
    continuar = input('Continuar [s] or [n]: ')

    if continuar == 'n':
        break
    else:
        continue
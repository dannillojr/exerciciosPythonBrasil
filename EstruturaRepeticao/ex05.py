# '''
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação
# '''

# '''
# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
# e escreva o número de anos necessários para que a população do país A ultrapasse 
# ou iguale a população do país B, mantidas as taxas de crescimento.
# '''

while True:
    
    pais_a = int(input('Digite a quantidade de habitantes atual de um país: '))
    crescimento_a = int(input('Digite a taxa de crescimento do país A em somente a parte inteira: '))

    pais_b = int(input('Digite a quantidade de habitantes atual de um outro país: '))
    crescimento_b = int(input('Digite a taxa de crescimento do país B em somente a parte inteira: '))

    taxa_a = crescimento_a / 100
    taxa_b = crescimento_b / 100

    anos = 0

    while pais_a <= pais_b:
        crescimento_anual_pais_a = taxa_a * pais_a
        crescimento_anual_pais_b = taxa_b * pais_b

        pais_a += crescimento_anual_pais_a
        pais_b += crescimento_anual_pais_b

        anos += 1  

    print(f'Vai demorar aproximadamente {anos} anos para pais [A] ser maior ou igual em população que o pais [B]')

    repetir = input('Deseja repetir [s] [n]: ')

    if repetir != 's':
        print('Encerrado')
        break




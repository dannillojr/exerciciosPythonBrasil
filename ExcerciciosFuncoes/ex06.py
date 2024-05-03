'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, 
a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas 
as vezes que desejar.

'''

def converte_tempo(hora):
    if hora >= 0 and hora < 12:
        return f'{hora:.2f} am'
    elif hora >= 12 and hora < 24:
        hora -= 12
        return f'{hora:.2f} pm'

def formata_exibicao(hora):
    nova_hora = str(hora).replace('.', ':')
    return nova_hora

while True:
    horas = float(input('Digite as horas separadas por [.] [-1 para encerrar]: '))

    if horas == -1:
        break
    else:
        if horas >= 24 or horas < 0:
            print('Hora inválida')
        else:
            horas_convertidas = converte_tempo(horas)
            print(formata_exibicao(horas_convertidas))



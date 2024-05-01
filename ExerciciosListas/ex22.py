'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:

1- necessita da esfera;
2- necessita de limpeza; 
3- necessita troca do cabo ou conector; 
4- quebrado ou inutilizado 


Uma identificação igual a zero encerra o programa. 
Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

identificacoes = {
    1: {'def': 'necessita da esfera'},
    2: {'def': 'necessita de limpeza'},
    3: {'def': 'trocar cabo ou conector'},
    4: {'def': 'quebrado ou inutilizado '},

}

id_mouses = []
cod_defeitos = []


print(f'{"ID":<10} {"SITUAÇÃO":<10}')
for chave, valor in identificacoes.items():
    print(f'{chave:<10} {valor['def']:<15}')

print('')

while True:
    try:
        id_mouse = int(input('QUAL O ID DO MOUSE: '))

        if id_mouse == 0:
            break
        defeito = int(input('DIGITE O COD DO DEFEITO: '))
        print('')
        if defeito not in identificacoes:
            print('')
            raise ValueError('Escolha um dos codigos exibidos acima')
            
            
        id_mouses.append(id_mouse)
        cod_defeitos.append(defeito)
        
    except ValueError as ve:
        print('ERROR' , ve)
        print('Insira uma entrada valida')
        print('')
        continue

contagem = {}

for num in cod_defeitos:

    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print('')
print(f'{"SITUAÇÂO":<28}{"QUANTIDADE":<15}{"PERCENTUAL":<15}')
for chave in contagem:
    porcentual = (contagem[chave] / len(cod_defeitos)) * 100
    print(f'{identificacoes[chave]["def"]:<28} {contagem[chave]:<15} {porcentual:.2f}%')


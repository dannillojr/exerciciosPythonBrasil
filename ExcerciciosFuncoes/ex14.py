'''
Quadrado mágico. 
Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, 
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
'''

def quadrado_magico():

    def verificar_se_e_quadrado_magico(lista):

        for i in range(0,9,3):
            if sum(lista[i:i+3]) != 15:
                return False
        
        for i in range(3):
            if lista[i] + lista[i+3] + lista[i+6] != 15:
                return False
            
        if lista[0] + lista[4] + lista[8] !=15:
            return False
        
        if lista[2] + lista[4] + lista[6] != 15:
            return False
        
        return True
    
    def permutacoes(lista):
        if len(lista) == 1:
            return [lista]
        else:
            resultado = []

            for i in range(len(lista)):
                primeiro = lista[i]
                restante = lista[:i] + lista[i+1:]
                for p in permutacoes(restante):
                    resultado.append([primeiro] + p)

            return resultado
    
    numeros = list(range(1,10))
    permu = permutacoes(numeros)

    for permutacao in permu:
        if verificar_se_e_quadrado_magico(permutacao):
            print(permutacao[0], permutacao[1], permutacao[2])
            print(permutacao[3], permutacao[4], permutacao[5])
            print(permutacao[6], permutacao[7], permutacao[8])
            print()

quadrado_magico()

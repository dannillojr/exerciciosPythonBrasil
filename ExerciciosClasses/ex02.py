'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado():

    def __init__(self):
        self.tamanho_lado = 10

    def mudar_valor_lado(self, novo_lado):
        self.tamanho_lado = novo_lado
        
        return self.tamanho_lado
    
    def mostrar_area(self):
        area = self.tamanho_lado * 2
        return area

quadrado1 = Quadrado()
quadrado1.mudar_valor_lado(20)

print(f'Os lados do quadrados são de {quadrado1.tamanho_lado}cm')

print(f'Sua area é de : {quadrado1.mostrar_area()}')



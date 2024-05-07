'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. 

Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para 
o local
'''

class Retangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Mudar_valor_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def Calcular_area(self):
        area = self.base *  self.altura

        return area

    def Calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)

        return perimetro
    

base = float(input('Digite a base do triangulo:'))
altura = float(input('Digite a altura do triangulo:'))

area_piso_padrao = 0.25
altura_rodape_padrao = 0.1


retangulo01 = Retangulo(base, altura)

area_retangulo01 = retangulo01.Calcular_area()
perimetro_retangulo01 = retangulo01.Calcular_perimetro()

qtd_piso = area_retangulo01//area_piso_padrao
qtd_rodape = altura_rodape_padrao * perimetro_retangulo01

print(f'Será necessario {qtd_piso}m² de piso para seu terreno')
print(f'Será necessario {qtd_rodape}m de {altura_rodape_padrao * 100}cm de rodape para seu terreno')
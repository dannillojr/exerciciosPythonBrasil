'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola():

    def __init__(self):
        self.cor = 'branca'
        self.circunferencia = 50
        self.material = 'carbono'

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor
    
bola1 = Bola()
bola2 = Bola()

bola1.trocaCor('rosa')
bola2.trocaCor('Preto')

print(bola1.mostraCor())
print(bola2.mostraCor())
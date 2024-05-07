'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        self.peso -= quilos
    
    def crescer(self, centimetros):
        self.altura += centimetros

# Exemplo de uso
pessoa1 = Pessoa('Danilo', 21, 100, 170)
pessoa1.envelhecer(2)

print(f'Nome: {pessoa1.nome}')
print(f'Idade: {pessoa1.idade} anos')
print(f'Peso: {pessoa1.peso}kg')
print(f'Altura: {pessoa1.altura}m')

print('')





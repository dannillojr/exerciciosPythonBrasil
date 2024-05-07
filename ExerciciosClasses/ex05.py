'''
Classe Conta Corrente: 
Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: 
número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class Conta_corrente():

    def __init__(self, numero_conta, nome, saldo=0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def Altera_nome(self, novo_nome):
        self.nome = novo_nome
    
    def Depositar(self, deposito):
        self.saldo += deposito
    
    def Sacar(self, saque):
        self.saldo -= saque

correntista_01 = Conta_corrente('001', 'JOSE')

correntista_01.Altera_nome('DANILOOO')
correntista_01.Depositar(100)
correntista_01.Sacar(50)

print(f'CONTA: {correntista_01.numero_conta}')
print(f'NOME: {correntista_01.nome}')
print(f'SALDO: {correntista_01.saldo}')
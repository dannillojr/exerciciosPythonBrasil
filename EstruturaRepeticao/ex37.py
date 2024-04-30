# '''
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
# Ao encerrar o programa também deve ser informados os códigos e valores do 
# clente mais alto, 
# do mais baixo, 
# do mais gordo 
# e do mais magro, 
# além da média das alturas 
# e dos pesos dos clientes
# '''

cod_mais_alto = None
cod_mais_baixo = None

cod_mais_gordo = None
cod_mais_magro = None

altura_mais_alto = 0
altura_mais_baixo = 0

peso_mais_gordo = 0
peso_mais_magro = 0

soma_alturas = 0
soma_peso = 0
contador = 0

while True:
    codigo = int(input('Qual seu codigo [0] para encerrar: '))
    print('')

    if codigo == 0:
        break

    altura = float(input('Qual sua altura: '))
    peso = float(input('Qual seu peso: '))
    print('')

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        cod_mais_alto = codigo

    if altura < altura_mais_baixo or altura_mais_baixo == 0:
        altura_mais_baixo = altura
        cod_mais_baixo = codigo
    
    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        cod_mais_gordo = codigo

    if peso < peso_mais_magro or peso_mais_magro == 0:
        peso_mais_magro = peso
        cod_mais_magro = codigo

    soma_alturas += altura
    soma_peso += peso
    contador += 1

media_altura = soma_alturas / contador
media_peso = soma_peso / contador

print('------------------Resultado------------------')
print('')
print(f'O cliente mais alto --> COD: {cod_mais_alto} altura: {altura_mais_alto}')
print(f'O cliente mais baixo --> COD: {cod_mais_baixo} altura: {altura_mais_baixo}')
print('')
print(f'O cliente mais gordo --> COD: {cod_mais_gordo} altura: {peso_mais_gordo}')
print(f'O cliente mais magro --> COD: {cod_mais_magro} altura: {peso_mais_magro}')
print('')
print(f'A media das alturas dessa academia é de {media_altura}')
print(f'A media dos pesos dessa academia é de {media_peso}')




    
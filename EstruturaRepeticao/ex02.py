# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

user = 'danilo'
passw = 123


while True:
    if user != login and passw != senha: 
        print('Dados incorretos tente novamente: ')
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
    
    else:
        print('Logado')
        break

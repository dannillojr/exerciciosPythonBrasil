# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salario: '))
sexo = input('Digite sexo [F] ou [M]: ')
estado_civil = input('Digite seu estado civil [S]-[C]-[V]-[D]: ')

while True:

    if len(nome) < 3:
      print('Não é um nome...')
      break

    elif idade < 0 and idade > 150:
      print('Idade invalida..')
      break

    elif salario < 0 :
      print('Salario invalido')
      break

    elif sexo != 'f' and sexo  != 'm':
      print('Sexo invalido')
      break

    elif estado_civil != 's' and  estado_civil != 'c' and  estado_civil != 'v' and  estado_civil != 'd':
      print('Estado civil invalido')
      break

    else :
      print(nome)
      print(idade)
      print(salario)
      print(sexo)
      print(estado_civil)
      break


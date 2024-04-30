'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321

'''

numeros = int(input('Digite um numero inteiro: '))

numeros_invertido = int(str(numeros)[::-1])

print(f'=> {numeros_invertido}')
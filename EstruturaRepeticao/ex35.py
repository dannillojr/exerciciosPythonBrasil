# '''
# Encontrar números primos é uma tarefa difícil. 
# Faça um programa que gera uma lista dos números 
# primos existentes entre 1 e um número inteiro informado pelo usuário.
# '''

    # for i in range(2, numero):
    #     primo = True
    #     for x in range(2, int(num**0.5) +1)
    #         if i % x == 0:
    #             primo = False
    #             break
    #     if primo:
    #         numeros_primos.append(num)




limite = int(input('Digite até onde quer a lista de numeros primos: '))

numeros_primos = []

for num in range(2, limite + 1):
    e_primo = True

    for x in range(2, int(num**0.5) + 1):

        if num % x == 0:
            e_primo = False
            break
        
    if e_primo:
        numeros_primos.append(num)

print(numeros_primos)
    
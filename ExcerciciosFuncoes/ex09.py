'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
'''

def inverter(num):
    str_num  = int(str(num)[::-1])
    
    return str_num

print(inverter(123))
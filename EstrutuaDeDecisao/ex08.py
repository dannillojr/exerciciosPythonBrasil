n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite mais um valor: '))

if n1 < n2 and n1 < n3:
    print(n1)

elif n2 < n1 and n2 < n3:
    print(n2)
    
else:
    print(n3)
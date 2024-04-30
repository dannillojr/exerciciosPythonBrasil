numeros_1 = [1,4,7,10,13]
numeros_2 = [2,5,8,11,14]
numeros_3 = [3,6,9,12,15]

numeros_intercalados = []

for i in range(5):
    
    numeros_intercalados.append(numeros_1[i])
    numeros_intercalados.append(numeros_2[i])
    numeros_intercalados.append(numeros_3[i])

print(numeros_intercalados)
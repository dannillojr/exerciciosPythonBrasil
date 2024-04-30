p1 = input("Telefonou para a vítima [sim] ou [não]? ")
p2 = input("Esteve no local do crime [sim] ou [não] ? ")
p3 = input("Mora perto da vítima [sim] ou [não] ? ")
p4 = input("Devia para a vítima[sim] ou [não] ? ")

lista_perguntas = [p1,p2,p3,p4]

quantidade_sim = lista_perguntas.count('sim') 
quantidade_não = lista_perguntas.count('não')

if quantidade_sim == 2:
    print('SUSPEITO...')
elif quantidade_sim == 3 or quantidade_sim == 4: 
    print('CUMPLICE...')
elif quantidade_sim == 5:
    print('CULPADO')
else:
    print('INOCENTE')
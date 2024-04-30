nota1 = float('Digite sua nota 01 : ')
nota2 = float('Digite sua nota 02 : ')


media = (nota1 +  nota2) / 2

if media >= 7:
    print(f'{media} --> APROVADO')
elif media < 7:
    print(f'{media} --> REPROVADO')
elif media == 10 :
    print(f'{media} -- > APROVADO COM DESTINÇÃO !!')
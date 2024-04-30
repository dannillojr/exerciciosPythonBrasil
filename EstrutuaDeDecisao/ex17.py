ano = int(input('Digite um ano: '))


if ano % 4 == 0:
    
    if ano % 100 != 0:
        print(f'{ano}: é bissexto')

        if ano % 400 == 0:
            print(f'{ano}: é bissexto')
else:
    print('não é bissexto')
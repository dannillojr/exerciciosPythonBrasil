data = input('digite a data de hoje: ')

dia, mes, ano = map(int, data.split('/'))

if dia > 0 and dia <= 31 and mes >= 1 and mes <= 12 and ano >= 1:
    print(f'Data valida {data}')
else:
    print(f'data invalida: {data} ')
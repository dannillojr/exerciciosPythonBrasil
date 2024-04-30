letra = input('Digite uma letra: ')

vogais = ['a', 'e', 'i', 'o', 'u']

if letra.lower() in vogais:
    print('A letra digita é uma vogal')
else:
    print('A letra digita é uma consoante')
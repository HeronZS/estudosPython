#aula23 foi sobre NOT


nome = input('Digite seu nome: ')
encontrar = input('Digite aquilo que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
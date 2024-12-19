#EXERCÍCIO


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaco = ' '


if nome:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')

    print(f'O seu nome invertido é: {nome[::-1]}')

    if espaco in nome:
        print('O seu nome contém espaço')

    else:
        print('O seu nome não contém espaço')

    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

elif not nome:
    print('Você não digitou seu nome!')
    
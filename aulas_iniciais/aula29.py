numero = input('Digite o número que será dobrado: ')



try:
    print(f'STR: {numero}')
    numero_int = int(numero)
    print(f'INT: {numero_int}')
    print(f'O dobro de {numero} é {numero_int * 2}')

except:
    print('Isso não é um número!')
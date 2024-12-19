while True:

    numero_1 = input('Digite o primeiro valor: ')
    numero_2 = input('Digite o segundo valor: ')
    operador = input('Digite o operador (+-*/): ')

    numeros_validos = None
    numero_1_flt = 0
    numero_2_flt = 0

    try:
        numero_1_flt = float(numero_1)
        numero_2_flt = float(numero_2)
        
        numeros_validos = True
        
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Confira o resultado do cálculo abaixo: ')
    
    if operador == '+':
        print(f'{numero_1_flt}+{numero_2_flt}= ', numero_1_flt + numero_2_flt)
    
    elif operador == '-':
        print(f'{numero_1_flt}-{numero_2_flt}= ', numero_1_flt - numero_2_flt)
    
    elif operador == '*':
        print(f'{numero_1_flt}*{numero_2_flt}= ', numero_1_flt * numero_2_flt)
    
    elif operador == '/':
        print(f'{numero_1_flt}/{numero_2_flt}= ', numero_1_flt / numero_2_flt)
    
    else:
        print('Isso não deveria ter acontecido')
        
    

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
            break
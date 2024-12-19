"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


            numero = input('Digite um número: ')

            try:
                numero_int = int(numero)
            
                numero_par = numero_int % 2 == 0
                numero_impar = numero_int % 2 != 0

                if numero_par:
                    print (f'O número {numero} é par')

                if numero_impar:
                    print(f'O número {numero} é ímpar')
                    
            except:
                print('O valor inserido não é inteiro') 




Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


            horario = input('Insira o horário atual: ')


            try:
                            
                horario_int = int(horario)
                            
                dia = horario_int >=0 and horario_int < 12
                tarde = horario_int >=12 and horario_int < 18
                noite = horario_int >=18 and horario_int < 24
                invalido = horario_int > 24
                            
                if dia:
                    print('Bom dia')
                            
                if tarde:
                    print('Boa tarde')
                                
                if noite:
                    print('Boa noite')
                        
                if invalido:
                    print('Esse horário não existe')
                                
            except:
                print('O valor inserido não é valido') 




Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""


nome = input('Digite seu nome: ')

nome_pequeno = len(nome) <= 4
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_grande = len(nome) > 6

if nome_pequeno:
    print('Seu nome é pequeno')

if nome_normal:
    print('Seu nome é normal')

if nome_grande:
    print('Seu nome é grande') 
    
    

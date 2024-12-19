num1 = input('Digite o primeiro valor ')
num2 = input('Digite o segundo valor ')

int_num1 = int(num1)
int_num2 = int(num2)

resultado = int_num1 / int_num2

if resultado % 2 == 0:
    print('O resultado é um número par')

elif resultado % 2 != 0:
    print('O resultado é um número ímpar')

else:
    print('Insira um valor válido!')


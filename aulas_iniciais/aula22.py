entrar = input ('[E]ntrar [S]air: ')
senha_digitada = input('Digite sua senha: ')

senha = '123456'

if entrar == 'E' or entrar =='e' and senha_digitada == senha:
    print('Login efetuado com sucesso')
else:
    print('Não foi possível fazer o login')
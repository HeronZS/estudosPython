# texto = 'Python'
# i = 0

# while i < len(texto):
#     print(texto[i])
    
#     i += 1


texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    
print (novo_texto + '*')
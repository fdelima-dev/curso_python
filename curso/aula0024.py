#Operadores in e not in
#strings interáveis

# nome = 'Felipe'
# print(nome[2])
# print(nome[-2])

# print('a' in nome)
# print('e' in nome)
# print('li' in nome)
# print('li' not in nome)
# print('vio' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
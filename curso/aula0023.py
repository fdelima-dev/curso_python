#not True = False
#not False = True
#usado para inverter expressões

senha = input('Senha: ')
if not senha:
    print('Você não digitou nada')

if senha != '123456':
    print('Senha incorreta')

#checagem de curto circuito
print(not True) #False
print(not False) #True
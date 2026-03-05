primeiro_valor = input('Digite um valor:\n')
segundo_valor = input('Digite outro valor:\n')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'{segundo_valor=}')
else:
    print(
        f'{segundo_valor=} é maior ou igual' 
        f'do que {primeiro_valor=}'
    )
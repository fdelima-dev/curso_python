"""
Formatação básica de strings
s - string
d - int
f - float
<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> esquerda
< direita
^ centro
sinal + ou -
Ex 0>-100,.1f
conversion flags !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:0^10}')
print(f'O Hexadecimal de 15 é {15:06X}')
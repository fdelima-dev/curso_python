"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        seu nome invertido é {nomeinvertido}
        seu nome contém ou não espaços
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
        Se nada for digitado em nome ou idade:
            exiba "Desculpe, você deixou campos vazios"
"""
nome = input('Digite seu nome\n')
idade = input('Digite sua idade\n')

variavel = nome
numero_letras = len(nome)
p_letra = nome[0]
u_letra = nome[-1]
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {variavel[::-1]}')
    print(f'Seu nome tem {numero_letras}')
    print(f'A primeira letra do seu nome é {p_letra}')
    print(f'A última letra do seu nome é {u_letra}')
    if " " in nome:
        print('Tem espaços')
    else:
        print('Não tem espaços')
elif nome or idade == '':
    print('Desculpe, você deixou campos vázios')

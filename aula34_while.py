'''
Repetições
While (enquanto)
Executar uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
'''

condicao = True


while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break # Para o o while mais proximo

print('Acabou')
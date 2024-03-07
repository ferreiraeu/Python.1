#                              Condicionais

# if / elif / else
# se / se não se / se não

entrada = input('Você deseja entrar no sistema ? ')


if entrada == 's':     # se eu ....
    print('Você entrou no sistema')
    
elif entrada == 'n':  # se não se acontecer ....
    print('Você saiu do sistema')

elif entrada == '':   # se não se acontecer ...
    print(' Tente somente S OU N')

else:                 # se não/então acontece isso...
    print('Você não digitou uma opção válida')

    
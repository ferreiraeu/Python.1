#                                              or


# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor



"""entrada = input('[E]ntrar[S]air]: ')
senha_digitada = input('senha: ')
senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and ( senha_digitada ):
    print('Realizou o Login ')

elif entrada == 'S' or entrada == 's':
    print('Você não realizou o login')

else:print('Dados não conferem')

"""
#senha = input('Senha:') or 'Sem senha' # aqui é feito como um if-else de forma simples
#print(senha)
#Avaliação de curto circuito

print( True or True or True)
print( True or False or True)
print( True or True or False)
print( False or False or False)


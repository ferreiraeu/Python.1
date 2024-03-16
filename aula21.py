#                                      and 


#Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor


"""entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrar')
else:
     print('Sair')
"""

#Avaliação de curto CIrcuito
print( True and True and True)
print( False and True and True)
print( True and False and True)
print( False and False and False)




#print(bool(1))

#if 0 and 1 : #O 0 (zero) de 0 and 1 avalia como falsy. O corpo do if não será executado.
 #   print(True and 1)
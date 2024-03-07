
#                       Introdução as variaveis Python


# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão
'''nome_completo = "Rogério ferreira"
soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)
print(nome_completo)
idade_completa = "06 11 1986"
print(nome_completo, idade_completa)'''

nome ='Rogério'
sobrenome ='Ferreira'
idade = 37
maior_de_idade = idade >= 18

print('Nome', nome, sobrenome)
print('Idade', idade)
if maior_de_idade == True:
     print('ta velho')
    
else :
     print('Ta novinho')
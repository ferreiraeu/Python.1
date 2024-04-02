''''
Flag (Bandeira ) - Marcar um local
None = Não valor
is e is not = é ou não é checa se é um => (tipo, valor, indentidade)
id = Indentidade (Pode ser o valor da memoria.)
'''

v1 = 'a'
v2 = 'a'
v3 = 'A'

print(id(v1))
print(id(v2))
print(id(v3))

''' Nota-se que os id tem a mesma localização  mesmo sendo com variáveis diferrentes no v1 e v2
Já o v3 já se torna difènte sua posição pois ele tem letra maiúscula.
'''

condicao = False

if condicao:
    print('Faça algo')
else:
    print('Não faça algo')
"""                       Interpolação de string com % em Python

Formatação com Interpolação básica de strings - paracido com o FORMAT
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""



nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) # nome é %s e preço é %.2f (Na duvida estudar placeholder)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) #%8x tranforma em hexadecimal
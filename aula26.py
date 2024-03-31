"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABCD'
print(f'{10000404.848475894494:,.1f}')
print(f'{variavel}')
print(f'.{variavel: >10}') # adicinei espaços a esquerda OBS> O PONTO É APENAS REFÊREMCIA
# print(f'{variavel: <10}.')
# print(f'{variavel: ^10}')
# print(f'{variavel:.^10}')
# print(f'{variavel:#^10}')
# print(f'{variavel:0^10}')

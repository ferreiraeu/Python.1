#                                            função len



"""
Fatiamento de strings
 012345678 
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] # i= inicio f= fim p= 
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo'
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[0:9:1])
print(variavel[0:9:4])
print(variavel[0:9:1])
print(variavel[-1:-10:-1])
print(variavel[::-1]) 



# print(variavel[5])
# print(variavel[5:])
# print(variavel[2:6])
# print(variavel[:6]) # sem inicio então conta do indice 0
# print(variavel[2:6])


# Fatiamento o final não é incluido, neste caso se precisa do indice 3 eu pego até o 4.

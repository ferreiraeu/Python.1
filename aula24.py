#                         (in) e (not in)

#Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2--1




#string = '0 1 2 3 4 5 6 7 8 9 10'
#nome = 'Otavio'
#print('o' in nome)
#print('10' not in string)
#print('10' in string)
#print('Ota' in nome)

#print(string[2]) 
#print(nome[-4])
#print(string[2]) 
#print(string[3]) 
#print(string[1]) # neste caso os epaços contam,assim quando imprime posição 1 é vazio e posição 2 é numero 1


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontra: ')

if encontrar in nome:
    print(f'{encontrar} enta em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
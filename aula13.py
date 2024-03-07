#                         Introdução às f-strings (formatação de strings)

nome = 'Rogério Ferreira'
altura = 1.86
peso = 98
imc = imc = peso / ( altura * altura )



print("   ")

nome = 'Rogério Ferreira'
altura = 1.86
peso = 98
imc = peso / ( altura * altura )


"f-strings" # São usados para formatação.
linha_1 = f'{nome} tem {altura:.2f} de altura e'
linha_2 = f'pesa {peso} quilos e seu imc é de'
linha_3 = f'{imc:.2f}' # Neste caso usamos pra obter a quantidade de casas depois da virgula.

print(linha_1)
print(linha_2)
print(linha_3)

print("   ")


#pode ser feito assim.
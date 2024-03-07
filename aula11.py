#                      Precedência entre os operadores aritméticos


# 1. (n + n)  ---- primeiro os parenteses.
# 2. **       ---- Depois a pontenciação.
# 3. * / // % ---- Depois a multiplicação, divisão, divisão indireta e modulo.(usando todas então e lida da esqueda pra direita).
# 4. + -      ---- por fim a adição e subtração.

conta_1 = 1 + 1 ** 5 + 5 #vamos organizar para dar o valor esperado.
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) 
print(conta_2)

conta_3 = ( 1 + (1 ** (5 + 5)) )
print(conta_3)


conta_3 = ( 1 + (1 ** 5) + 5)
print(conta_3)

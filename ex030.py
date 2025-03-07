# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número qualquer: '))
resultado = num % 2 # resto da divisão
if  resultado == 0: # se o resto da divisão for 0
    print('O número {} é PAR'.format(num))

else:
    print('O número {} é ÍMPAR'.format(num))


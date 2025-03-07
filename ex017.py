# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
o = float(input('Qual o Comprimento do Cateto Oposto? '))
a = float(input('Qual o Comprimento do Cateto Adjacente? '))
hi = math.hypot(o, a)
print('A hipotenusa vai medir {:.2f}'.format(hi))

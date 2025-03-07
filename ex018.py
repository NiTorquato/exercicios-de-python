# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(angulo))
c = math.cos(math.radians(angulo))
t = math.tan(math.radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, s))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, c))
print('O ângulo de {} tem TÂNGENTE de {:.2f}'.format(angulo, t))

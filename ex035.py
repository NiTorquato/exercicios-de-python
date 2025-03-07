# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*12)
print('Analisador de Triângulos')
print('-='*12)

a = float(input('\033[1;33mPrimeiro segmento:\033[m '))
b = float(input('\033[1;31mSegundo segmento: \033[m'))
c = float(input('\033[1;32mTerceiro segmento: \033[m'))

if a + b > c and a + c > b and b + c > a:
            print('Os segmento acima podem formar triângulo! ')

else:
            print('Os segmentos acima não podem formar triângulo! ')

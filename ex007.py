#Desenvolva um programa que leia duas notas de um aluno, calcule e leia sua média

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

# Média
m = (n1 + n2) / 2

print('A média das notas {} e {} é igual a {:.1f}: '.format(n1, n2, m))

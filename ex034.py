# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$'))
reais = 1250
if salario <= reais:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)

print('Quem ganhava \033[1;33mR${:.2f}\033[m passara a ganhar \033[1;32mR${:.2f}\033[m agora'.format(salario, aumento))

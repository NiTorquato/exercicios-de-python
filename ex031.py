# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Qual é a distâcia da sua viagem? '))
print('Você está preste a começar uma viagem de {:.2f}Km'.format(viagem))
km = 200
if viagem <= km:
    valor = viagem * 0.50

else:
    valor = viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}:'.format(valor))
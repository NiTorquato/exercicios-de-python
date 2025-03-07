# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

carro = int(input('Qual a velocidade atual do Carro? '))
velocidade = 80 # Limite da velocidade
if carro > velocidade:
    exedido = carro - velocidade # Calcula velocidade exedida
    multa = 7 * exedido # Calcula Multa
    print('Multado! Você excedeu o limite de velocidade que é de 80 km/h')
    print('Você deve pagar uma multa de R$ {:.2f} '.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')
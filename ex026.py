# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma Frase: ')).strip().upper()
print('Sua frase tem ao todo {} letras A'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1))

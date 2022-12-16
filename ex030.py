# Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é PAR!')
elif num % 2 == 1:
    print(f'O número {num} é ÍMPAR!')

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
# Verificando o maior
if num1 > num2 and num1 > num3:
    print(f'O MAIOR valor digitado foi {num1}!')
if num2 > num1 and num2 > num3:
    print(f'O MAIOR valor digitado foi {num2}!')
if num3 > num1 and num3 > num2:
    print(f'O MAIOR valor digitado foi {num3}!')
# Verificando o menor
if num1 < num2 and num1 < num3:
    print(f'O MENOR valor digitado foi {num1}!')
if num2 < num1 and num2 < num3:
    print(f'O MENOR valor digitado foi {num2}!')
if num3 < num1 and num3 < num2:
    print(f'O MENOR valor digitado foi {num3}!')

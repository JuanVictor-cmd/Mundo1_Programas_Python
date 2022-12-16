# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número inteiro: '))
print('-'*12)
for x in range(11):
    mul = num * x
    print(f'{num} X {x} = {mul}')
print('-'*12)

# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o seu salário: R$'))
novo_salario = (salario * 15 / 100) + salario
print(f'Novo Salário: R${novo_salario:.2f}')

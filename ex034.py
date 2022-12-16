# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário: R$'))

if salario >= 1250.00:
    novo_salario = (salario * 10 / 100) + salario
    print(
        f'Quem ganhava R${salario:.2f} agora passa a receber R${novo_salario:.2f}')
else:
    novo_salario = (salario * 15 / 100) + salario
    print(
        f'Quem ganhava R${salario:.2f} agora passa a receber R${novo_salario:.2f}')

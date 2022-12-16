# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere U$1.00 = R$3,27.

carteira = float(input('Digite o valor do dinheiro em sua carteira: R$'))
dolar = carteira / 3.27
print(f'Você pode comprar U${dolar:.2f} dólares')

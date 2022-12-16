# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = float(input('Digite o preço do produto: R$'))
desconto = (produto * 5 / 100)
print(f'Desconto de 5%: R${desconto:.2f}')
total = produto - desconto
print(f'Novo Preço: R${total:.2f}')

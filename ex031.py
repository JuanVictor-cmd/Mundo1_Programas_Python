# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.

viagem = float(input('Qual é a distância da sua viagem: '))

if viagem <= 200:
    preço = viagem * 0.50
    print(f'Você está prestes a começar uma viagem de {viagem}Km/h.')
    print(f'E o preço da sua passagem será de R${preço:.1f}')
else:
    desconto = viagem * 0.45
    print(f'Você está prestes a começar uma viagem de {viagem}Km/h.')
    print(f'E o preço da sua passagem será de R${desconto:.1f}')

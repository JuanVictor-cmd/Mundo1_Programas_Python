# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km = float(input('Digite a quantidade de Km corridos: '))
Dias = float(input('Digite a quantidade de dias pelo qual ele foi alugado: '))
pago = (60 * Dias) + (0.15 * Km)
print(
    f'Km Corridos: {Km:.0f} Km/h\nDias Alugados: {Dias:.0f} Dias\nTotal a Pagar: R${pago:.2f}')

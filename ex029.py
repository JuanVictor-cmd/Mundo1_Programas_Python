# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km
# acima do limite.

carro = int(input('Qual é a velocidade atual do carro? '))
if carro <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (carro - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada metro de tinta , pinta uma área de 2m².

largura = float(input('Digite a largura em metros da sua parede: '))
altura = float(input('Digite a altura em metros da sua parede: '))
area = (altura * largura)
tinta = area / 2
print(f'Largura: {largura}')
print(f'Altura: {altura}')
print(f'Área: {area}m²\nTinta necessária para pintar a parede: {tinta}L')

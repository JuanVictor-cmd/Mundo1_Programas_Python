# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Digite um valor em metros: '))
centimetros = metros*100
milimetros = metros*1000
print('Centímetros: {}\nMilímetros: {}'.format(centimetros, milimetros))

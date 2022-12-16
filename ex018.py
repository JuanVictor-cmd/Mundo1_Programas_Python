# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, acos, atan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem o SENO de: {seno:.2f}')
cosseno = acos(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem o COSSENO de: {cosseno:.2f}')
tangente = atan(radians(angulo))
print(f'O ângulo de {angulo:.2f} tem a TANGENTE de: {tangente:.2f}')

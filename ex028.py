# Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
from random import randint
from time import sleep
computador = randint(0, 5)
print('-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-'*20)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == computador:
    print(f'PARABÉNS!! o número que pensei foi {computador}!')
else:
    print(f'ERROU! o número que pensei foi {computador} e não {numero}!')

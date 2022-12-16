# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Onde: F=9/5C+32

celsius = float(input('Digite a temperatura °C: '))
faren = (celsius*9/5)+32
print(f'A temperatura em °F: {faren}')

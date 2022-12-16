# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
print('-' * 20)
print('Analisador de Triângulos')
print('-' * 20)
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
#  e menor que a soma dos outros dois lados. Veja o resumo da regra abaixo:
# |b-c|<a<b+c
# |a-c|<b<a+c
# |a-b|<c<a+b
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!!')

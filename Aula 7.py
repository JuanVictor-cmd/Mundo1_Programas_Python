nome = str(input('Qual o seu nome: '))
print('Prazer em te conhecer {:>20}'.format(nome))
print(f'Prazer em te conhecer {nome:>20}')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
print(
    f'A soma vale {soma}, a subtração vale {sub}, a multiplicação vale {mul:.2f}.', end=' ')
print('A divisão vale {} e a potência vale {:.2f}.'.format(div, pot))

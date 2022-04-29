number = int(input('Digite um valor para calcular o seu Fatorial: '))
count = number
fator = 1
print('Calculando {}!'.format(number))
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    fator *= count 
    count -= 1
print (fator)
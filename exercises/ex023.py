from math import trunc
n = float(input('Insira um numero de 0 a 9999: '))
if n > 9999:
    print('O número {} é maior que 9999.'.format(n))
else:
    x = str(trunc(n))
    print('O numero escolhido foi {}!'.format(n))
    if len(x) == 4:
        print('Unidade: {}'.format(x[3]))
        print('Dezena: {}'.format(x[2]))
        print('Centena: {}'.format(x[1]))
        print('Milhar: {}'.format(x[0]))
    elif len(x) == 3:
        print('Unidade: {}'.format(x[2]))
        print('Dezena: {}'.format(x[1]))
        print('Centena: {}'.format(x[0]))
    elif len(x) == 2:
        print('Unidade: {}'.format (x[1]))
        print('Dezena: {}'.format(x[0]))
    else:
        print('Unidade: {}'.format(x[0]))
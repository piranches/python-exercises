number = float(input('Insira um número de 0 a 9999: '))
if number > 9999:
    print('The number entered is higher than 9999.')
else:
    unity = number // 1 % 10
    ten = number // 10 % 10
    hundred = number // 100 % 10
    thousand = number // 1000 % 10
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unity,ten,hundred,thousand))
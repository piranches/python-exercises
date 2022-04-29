print('Descubra se o ano é {}BISSEXTO{}!'.format('\033[1;33m','\033[m'))
year = int(input('Insira o ano desejado aqui: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} {}É BISSEXTO{}!'.format(year,'\033[1;33m','\033[m'))
else:
    print('O ano {} {}NÃO É BISSEXTO{}!'.format(year,'\033[1;33m','\033[m'))
